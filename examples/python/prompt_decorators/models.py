"""Core models for the Prompt Decorators implementation."""

from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, constr


class DecoratorMetadata(BaseModel):
    """Metadata for a decorator instance."""
    description: Optional[str] = None
    category: Optional[str] = None
    deprecated: bool = False
    deprecationMessage: Optional[str] = None

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to exclude deprecationMessage when not deprecated."""
        data = super().model_dump(**kwargs)
        if not data.get("deprecated", False):
            data.pop("deprecationMessage", None)
        return data

    class Config:
        """Pydantic configuration."""
        json_encoders = {
            Optional[str]: lambda v: v if v is not None else None
        }
        exclude_none = True


class BaseDecorator(BaseModel):
    """Base model for all decorators."""
    name: constr(pattern=r"^[A-Z][a-zA-Z0-9]*$") = Field(..., description="Name of the decorator")
    version: constr(pattern=r"^\d+\.\d+\.\d+$") = Field("1.0.0", description="Version of the decorator")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Parameters for the decorator")
    metadata: Optional[DecoratorMetadata] = None

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to properly serialize enum values."""
        data = super().model_dump(**kwargs)
        if "parameters" in data:
            data["parameters"] = {
                k: v.value if isinstance(v, Enum) else v
                for k, v in data["parameters"].items()
            }
        return data

    class Config:
        """Pydantic configuration."""
        json_encoders = {
            Optional[str]: lambda v: v if v is not None else None
        }
        exclude_none = True


class OutputFormat(str, Enum):
    """Supported output formats."""
    JSON = "json"
    MARKDOWN = "markdown"
    YAML = "yaml"
    XML = "xml"
    TEXT = "text"


class ToneStyle(str, Enum):
    """Supported tone styles."""
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    ACADEMIC = "academic"
    FRIENDLY = "friendly"
    FORMAL = "formal"


class ReasoningDecorator(BaseDecorator):
    """Reasoning decorator for detailed explanation of reasoning process."""
    name: str = "Reasoning"
    parameters: Dict[str, Any] = Field(
        default_factory=lambda: {"depth": "standard"},
        description="Parameters for reasoning process"
    )


class StepByStepDecorator(BaseDecorator):
    """StepByStep decorator for structured, sequential responses."""
    name: str = "StepByStep"
    parameters: Dict[str, Any] = Field(
        default_factory=lambda: {"numbered": True},
        description="Parameters for step-by-step formatting"
    )


class OutputFormatDecorator(BaseDecorator):
    """OutputFormat decorator for specifying response format."""
    name: str = "OutputFormat"
    parameters: Dict[str, Any] = Field(
        ...,
        description="Parameters for output formatting",
        example={"format": "json"}
    )


class ToneDecorator(BaseDecorator):
    """Tone decorator for adjusting response style."""
    name: str = "Tone"
    parameters: Dict[str, Any] = Field(
        ...,
        description="Parameters for tone adjustment",
        example={"style": "professional"}
    )


class VersionDecorator(BaseDecorator):
    """Version decorator for specifying standard compliance."""
    name: str = "Version"
    parameters: Dict[str, Any] = Field(
        ...,
        description="Parameters for version specification",
        example={"standard": "1.0.0"}
    )


class APIRequest(BaseModel):
    """Model for API requests using decorators."""
    prompt: str = Field(..., description="The prompt text")
    decorators: List[Union[
        ReasoningDecorator,
        StepByStepDecorator,
        OutputFormatDecorator,
        ToneDecorator,
        VersionDecorator
    ]] = Field(default_factory=list, description="List of decorators to apply")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata for the request"
    )

    class Config:
        """Pydantic configuration."""
        json_encoders = {
            Optional[str]: lambda v: v if v is not None else None
        }
        exclude_none = True 