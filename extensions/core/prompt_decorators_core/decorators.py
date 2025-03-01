"""
Decorator classes for the Prompt Decorators Core extension package.
"""

from enum import Enum
from typing import Dict, Optional, Any, TypedDict


class ReasoningDepth(str, Enum):
    """Depth options for the Reasoning decorator."""
    BASIC = "basic"
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive"


class OutputFormatType(str, Enum):
    """Format options for the OutputFormat decorator."""
    PLAINTEXT = "plaintext"
    MARKDOWN = "markdown"
    JSON = "json"
    YAML = "yaml"
    XML = "xml"


class ToneStyle(str, Enum):
    """Style options for the Tone decorator."""
    FORMAL = "formal"
    CASUAL = "casual"
    FRIENDLY = "friendly"
    TECHNICAL = "technical"
    HUMOROUS = "humorous"


class DecoratorMetadata(TypedDict, total=False):
    """Metadata for a decorator."""
    category: str
    deprecated: bool
    deprecationMessage: str


class BaseDecorator:
    """Base class for all decorators."""
    
    def __init__(
        self,
        name: str,
        version: str = "1.0.0",
        parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize a decorator.
        
        Args:
            name: The name of the decorator.
            version: The version of the decorator.
            parameters: Optional parameters for the decorator.
            metadata: Optional metadata for the decorator.
        """
        self.name = name
        self.version = version
        self.parameters = parameters or {}
        self.metadata = metadata or {"category": "core"}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.
        
        Returns:
            A dictionary representation of the decorator.
        """
        result = {
            "name": self.name,
            "version": self.version,
            "parameters": self.parameters,
            "metadata": self.metadata
        }
        return result
    
    def to_string(self) -> str:
        """
        Convert the decorator to a string.
        
        Returns:
            A string representation of the decorator.
        """
        from .utils import format_parameter_value
        params_str = ", ".join(f"{k}={format_parameter_value(v)}" for k, v in self.parameters.items())
        return f"+++{self.name}({params_str})"


class Reasoning(BaseDecorator):
    """
    Decorator for showing reasoning process in responses.
    
    This decorator encourages the AI to show its thought process before reaching conclusions.
    """
    
    def __init__(
        self,
        depth: ReasoningDepth = ReasoningDepth.MODERATE,
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize a Reasoning decorator.
        
        Args:
            depth: The level of detail in the reasoning process.
            metadata: Optional metadata for the decorator.
        """
        super().__init__(
            name="Reasoning",
            parameters={"depth": depth},
            metadata=metadata
        )


class StepByStep(BaseDecorator):
    """
    Decorator for structuring responses as a sequence of steps.
    
    This decorator helps break down complex processes into manageable steps.
    """
    
    def __init__(
        self,
        numbered: bool = True,
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize a StepByStep decorator.
        
        Args:
            numbered: Whether to number the steps.
            metadata: Optional metadata for the decorator.
        """
        super().__init__(
            name="StepByStep",
            parameters={"numbered": numbered},
            metadata=metadata
        )


class OutputFormat(BaseDecorator):
    """
    Decorator for controlling the format of responses.
    
    This decorator ensures consistent formatting across different use cases.
    """
    
    def __init__(
        self,
        format: OutputFormatType = OutputFormatType.PLAINTEXT,
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize an OutputFormat decorator.
        
        Args:
            format: The desired output format.
            metadata: Optional metadata for the decorator.
        """
        super().__init__(
            name="OutputFormat",
            parameters={"format": format},
            metadata=metadata
        )


class Tone(BaseDecorator):
    """
    Decorator for adjusting the writing style of responses.
    
    This decorator helps ensure responses are appropriately styled for different audiences.
    """
    
    def __init__(
        self,
        style: ToneStyle = ToneStyle.FORMAL,
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize a Tone decorator.
        
        Args:
            style: The desired tone and style.
            metadata: Optional metadata for the decorator.
        """
        super().__init__(
            name="Tone",
            parameters={"style": style},
            metadata=metadata
        )


class Version(BaseDecorator):
    """
    Decorator for specifying the version of the Prompt Decorators standard.
    
    This decorator ensures proper interpretation of decorators according to the specified version.
    """
    
    def __init__(
        self,
        standard: str = "1.0.0",
        metadata: Optional[DecoratorMetadata] = None
    ):
        """
        Initialize a Version decorator.
        
        Args:
            standard: The semantic version of the standard to use.
            metadata: Optional metadata for the decorator.
        """
        super().__init__(
            name="Version",
            parameters={"standard": standard},
            metadata=metadata
        ) 