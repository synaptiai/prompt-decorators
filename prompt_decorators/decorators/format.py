"""
Output Format Decorator

This decorator controls the output format of the model response.
"""

from enum import Enum
from typing import Dict, Any, Optional, List

from ..core.base import BaseDecorator, ValidationError


class FormatType(Enum):
    """Enumeration of output format types."""
    TEXT = "text"
    MARKDOWN = "markdown"
    JSON = "json"
    HTML = "html"
    CSV = "csv"
    YAML = "yaml"
    XML = "xml"


class OutputFormat(BaseDecorator):
    """
    Decorator that controls the output format of the model response.
    
    This decorator specifies the format of the model's output, such as:
    - Plain text
    - Markdown
    - JSON
    - HTML
    - CSV
    - YAML
    - XML
    """
    
    name = "OutputFormat"
    description = "Controls the output format of the model response"
    category = "OutputModifiers"
    version = "1.0.0"
    min_compatible_version = "1.0.0"
    
    def __init__(
        self,
        format_type: str = FormatType.TEXT.value,
        schema: Optional[Dict[str, Any]] = None,
        headers: Optional[List[str]] = None,
        pretty_print: bool = True,
        name: Optional[str] = None,
        version: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize an OutputFormat decorator.
        
        Args:
            format_type: Type of output format (text, markdown, json, etc.)
            schema: Optional schema for structured formats (JSON, XML)
            headers: Optional headers for tabular formats (CSV)
            pretty_print: Whether to pretty-print the output
            name: Optional decorator name override
            version: Optional version override
            parameters: Optional parameter dictionary (overrides individual parameters)
            metadata: Optional metadata dictionary
        """
        # If parameters are explicitly provided, use them instead of individual args
        if parameters is None:
            parameters = {
                "format_type": format_type,
                "schema": schema,
                "headers": headers,
                "pretty_print": pretty_print
            }
        
        super().__init__(name, version, parameters, metadata)
    
    def validate(self) -> None:
        """
        Validate decorator parameters.
        
        Raises:
            ValidationError: If any parameter fails validation
        """
        # Validate format type parameter
        format_type = self._validate_enum("format_type", FormatType)
        
        # Validate schema parameter if format type requires it
        if format_type in [FormatType.JSON, FormatType.XML, FormatType.YAML]:
            self._validate_type("schema", dict, allow_none=True)
        
        # Validate headers parameter if format type is CSV
        if format_type == FormatType.CSV:
            headers = self.parameters.get("headers")
            if headers is not None and not isinstance(headers, list):
                raise ValidationError(
                    self.name, "headers", f"Expected list, got {type(headers).__name__}"
                )
        
        # Validate boolean parameters
        self._validate_type("pretty_print", bool)
    
    def apply(self, prompt: str) -> str:
        """
        Apply the output format decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with output format instructions
        """
        format_type = self._validate_enum("format_type", FormatType)
        schema = self.parameters.get("schema")
        headers = self.parameters.get("headers")
        pretty_print = self._validate_type("pretty_print", bool)
        
        # Base instruction
        instruction = f"Format your response as {format_type.value}."
        
        # Add format-specific instructions
        if format_type == FormatType.MARKDOWN:
            instruction += " Use proper markdown syntax with headings, lists, code blocks, and emphasis where appropriate."
        
        elif format_type == FormatType.JSON:
            instruction += " Return valid, parseable JSON."
            if schema:
                schema_str = str(schema).replace("'", '"')
                instruction += f" Follow this schema: {schema_str}."
        
        elif format_type == FormatType.HTML:
            instruction += " Use proper HTML tags and structure."
            if pretty_print:
                instruction += " Include appropriate indentation and spacing for readability."
        
        elif format_type == FormatType.CSV:
            if headers:
                headers_str = ", ".join(headers)
                instruction += f" Include the following headers: {headers_str}."
            instruction += " Separate values with commas and rows with newlines."
        
        elif format_type == FormatType.YAML:
            instruction += " Use proper YAML syntax with correct indentation."
            if schema:
                schema_str = str(schema).replace("'", '"')
                instruction += f" Follow this schema: {schema_str}."
        
        elif format_type == FormatType.XML:
            instruction += " Use well-formed XML with proper tags and structure."
            if schema:
                schema_str = str(schema).replace("'", '"')
                instruction += f" Follow this structure: {schema_str}."
        
        # Add pretty print instruction if applicable
        if pretty_print and format_type in [FormatType.JSON, FormatType.XML, FormatType.YAML]:
            instruction += " Format the output with proper indentation and line breaks for readability."
        
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}" 