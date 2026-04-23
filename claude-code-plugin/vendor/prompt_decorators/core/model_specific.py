"""Model-Specific Decorator Module.

This module provides base classes and utilities for model-specific decorator adaptations.
"""
import logging
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.model_detection import get_model_detector

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


T = TypeVar("T", bound=BaseDecorator)


class ModelSpecificDecorator(BaseDecorator, Generic[T]):
    """Base class for model-specific decorator adaptations.

    This class extends BaseDecorator to support model-specific adaptations,
    allowing decorators to adjust their behavior based on the model being used.
    """

    def __init__(self, model_id: Optional[str] = None, **kwargs):
        """Initialize a model-specific decorator.

        Args:
            model_id: ID of the model to adapt for (optional)
            **kwargs: Additional parameters for the decorator. These are passed to the parent class constructor.
        """
        # Initialize the base decorator
        super().__init__(**kwargs)

        # Store the model ID
        self.model_id = model_id

        # Get model capabilities if a model ID was provided
        self.model_capabilities = None
        if model_id:
            self.model_capabilities = get_model_detector().get_model_capabilities(
                model_id
            )

    def set_model(self, model_id: str) -> None:
        """Set the model ID for this decorator.

        Args:
            model_id: ID of the model to adapt for

        Returns:
            None
        """
        self.model_id = model_id
        self.model_capabilities = get_model_detector().get_model_capabilities(model_id)

    def is_supported_by_model(self) -> bool:
        """Check if this decorator is supported by the current model.

        Args:
            self: The decorator instance

        Returns:
            True if supported, False otherwise
        """
        if not self.model_id or not self.model_capabilities:
            # If no model is specified, assume support
            return True

        # Check if the model has a list of supported decorators
        if "supported_decorators" in self.model_capabilities.capabilities:
            # If the model has a list of supported decorators, check if this decorator is in it
            supported = (
                self.name
                in self.model_capabilities.capabilities["supported_decorators"]
            )
            return supported

        # If no specific support information, assume support
        return True

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt with model-specific adaptations.

        This implementation first checks if the decorator is supported by the model,
        then delegates to either apply_for_model or apply_fallback based on support.

        Args:
            prompt: The original prompt to decorate

        Returns:
            The decorated prompt
        """
        if self.is_supported_by_model():
            # Model supports this decorator
            return self.apply_for_model(prompt)
        else:
            # Model doesn't support this decorator, use fallback
            return self.apply_fallback(prompt)

    def apply_for_model(self, prompt: str) -> str:
        """Apply the decorator with model-specific adaptations.

        This method should be implemented by subclasses to provide
        model-specific adaptations.

        Args:
            prompt: The original prompt to decorate

        Returns:
            The decorated prompt
        """  # Default implementation - subclasses should override this
        return f"Model-specific adaptation for {self.name} with model {self.model_id}:\n\n{prompt}"

    def apply_fallback(self, prompt: str) -> str:
        """Apply a fallback decoration when model doesn't support this decorator.

        This method provides a fallback implementation that still attempts to
        achieve a similar effect, but with simplified instructions.

        Args:
            prompt: The original prompt to decorate

        Returns:
            The decorated prompt
        """  # Default fallback - subclasses should override this
        fallback_note = f"Note: The {self.name} decorator is not fully supported by this model. Using simplified instructions."
        return f"{fallback_note}\n\n{prompt}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        data = super().to_dict()
        data["model_id"] = self.model_id
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModelSpecificDecorator":
        """Create a decorator from a dictionary.

        Args:
            data: Dictionary representation of the decorator

        Returns:
            New decorator instance
        """
        model_id = data.get("model_id")
        parameters = data.get("parameters", {})

        return cls(model_id=model_id, **parameters)


class ModelSpecificDecoratorFactory:
    """Factory for creating model-specific decorators.

    This class provides methods for creating model-specific versions of decorators.
    It allows for customizing decorator behavior based on specific model requirements.

    The factory creates decorator instances that are tailored to work optimally with
    particular language models, taking into account their unique capabilities and limitations.
    """

    @staticmethod
    def create_for_model(
        decorator_class: Type[BaseDecorator], model_id: str, **params
    ) -> BaseDecorator:
        """Create a model-specific version of a decorator.

        This method creates a new class that extends both ModelSpecificDecorator and
        the original decorator class, allowing for model-specific adaptations.

        Args:
            decorator_class: Original decorator class
            model_id: ID of the model to adapt for
            **params: Parameters for the decorator. These are passed to the decorator constructor.

        Returns:
            Instance of the model-specific decorator
        """  # Create a name for the model-specific class
        model_specific_name = f"{decorator_class.__name__}_{model_id.replace('-', '_')}"

        # Create a new class that inherits from both ModelSpecificDecorator and the original class
        model_specific_class = type(
            model_specific_name,
            (ModelSpecificDecorator, decorator_class),
            {
                "__init__": lambda self, **kwargs: ModelSpecificDecorator.__init__(
                    self, model_id=model_id, **kwargs
                ),
                "apply_for_model": lambda self, prompt: decorator_class.apply(
                    self, prompt
                ),
                "_model_id": model_id,
            },
        )

        # Create an instance of the new class
        return model_specific_class(**params)
