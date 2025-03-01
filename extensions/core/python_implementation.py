#!/usr/bin/env python3
"""
Python implementation for the Prompt Decorators Core extension package.

This module provides classes and functions for working with the core decorators
in Python applications.
"""

from enum import Enum
from typing import Dict, List, Optional, Union, Any, Literal, TypedDict, cast
import json
import re


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


def format_parameter_value(value: Any) -> str:
    """
    Format a parameter value for string representation.
    
    Args:
        value: The parameter value to format.
        
    Returns:
        A string representation of the parameter value.
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, Enum):
        return value.value
    elif isinstance(value, str):
        if " " in value:
            return f'"{value}"'
        return value
    return str(value)


def parse_decorator_string(decorator_str: str) -> Optional[BaseDecorator]:
    """
    Parse a decorator string into a decorator object.
    
    Args:
        decorator_str: The decorator string to parse.
        
    Returns:
        A decorator object, or None if the string could not be parsed.
    """
    # Match the decorator pattern: +++Name(param1=value1, param2=value2)
    pattern = r"^\+\+\+([A-Za-z][A-Za-z0-9]*)\(?(.*?)\)?$"
    match = re.match(pattern, decorator_str.strip())
    
    if not match:
        return None
    
    name = match.group(1)
    params_str = match.group(2)
    
    # Parse parameters
    parameters = {}
    if params_str:
        for param in params_str.split(","):
            param = param.strip()
            if not param:
                continue
                
            key_value = param.split("=", 1)
            if len(key_value) != 2:
                continue
                
            key, value = key_value
            key = key.strip()
            value = value.strip()
            
            # Convert value to appropriate type
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            
            parameters[key] = value
    
    # Create the appropriate decorator based on the name
    if name == "Reasoning":
        depth = parameters.get("depth", ReasoningDepth.MODERATE)
        return Reasoning(depth=depth)
    elif name == "StepByStep":
        numbered = parameters.get("numbered", True)
        return StepByStep(numbered=numbered)
    elif name == "OutputFormat":
        format_value = parameters.get("format", OutputFormatType.PLAINTEXT)
        return OutputFormat(format=format_value)
    elif name == "Tone":
        style = parameters.get("style", ToneStyle.FORMAL)
        return Tone(style=style)
    elif name == "Version":
        standard = parameters.get("standard", "1.0.0")
        return Version(standard=standard)
    
    # Generic decorator for unknown types
    return BaseDecorator(name=name, parameters=parameters)


def apply_decorators(decorators: List[BaseDecorator], prompt: str) -> str:
    """
    Apply decorators to a prompt.
    
    Args:
        decorators: List of decorators to apply.
        prompt: The prompt to decorate.
        
    Returns:
        The decorated prompt.
    """
    result = ""
    for decorator in decorators:
        result += decorator.to_string() + "\n"
    
    result += prompt
    return result


def convert_decorators_to_system_instructions(decorators: List[BaseDecorator]) -> str:
    """
    Convert decorators to system instructions for an LLM.
    
    Args:
        decorators: List of decorators to convert.
        
    Returns:
        System instructions for the LLM.
    """
    instructions = [
        "You are an AI assistant that follows instructions precisely.",
        "Please adhere to the following requirements when generating your response:"
    ]
    
    for decorator in decorators:
        if decorator.name == "Reasoning":
            depth = decorator.parameters.get("depth", ReasoningDepth.MODERATE)
            if depth == ReasoningDepth.BASIC:
                instructions.append("- Show basic reasoning before reaching conclusions.")
            elif depth == ReasoningDepth.MODERATE:
                instructions.append("- Show moderate reasoning before reaching conclusions, explaining your thought process.")
            elif depth == ReasoningDepth.COMPREHENSIVE:
                instructions.append("- Show comprehensive reasoning before reaching conclusions, with detailed explanations of your thought process, considering multiple perspectives and potential objections.")
        
        elif decorator.name == "StepByStep":
            numbered = decorator.parameters.get("numbered", True)
            if numbered:
                instructions.append("- Structure your response as a sequence of numbered steps.")
            else:
                instructions.append("- Structure your response as a sequence of bullet point steps.")
        
        elif decorator.name == "OutputFormat":
            format_value = decorator.parameters.get("format", OutputFormatType.PLAINTEXT)
            if format_value == OutputFormatType.MARKDOWN:
                instructions.append("- Format your response using Markdown syntax.")
            elif format_value == OutputFormatType.JSON:
                instructions.append("- Format your response as a valid JSON object.")
            elif format_value == OutputFormatType.YAML:
                instructions.append("- Format your response as a valid YAML document.")
            elif format_value == OutputFormatType.XML:
                instructions.append("- Format your response as a valid XML document.")
            else:
                instructions.append("- Format your response as plain text.")
        
        elif decorator.name == "Tone":
            style = decorator.parameters.get("style", ToneStyle.FORMAL)
            if style == ToneStyle.FORMAL:
                instructions.append("- Use a formal, professional tone in your response.")
            elif style == ToneStyle.CASUAL:
                instructions.append("- Use a casual, relaxed tone in your response.")
            elif style == ToneStyle.FRIENDLY:
                instructions.append("- Use a friendly, warm tone in your response.")
            elif style == ToneStyle.TECHNICAL:
                instructions.append("- Use a technical, precise tone with appropriate terminology in your response.")
            elif style == ToneStyle.HUMOROUS:
                instructions.append("- Use a light-hearted, witty tone in your response.")
    
    return "\n".join(instructions)


class APIRequest:
    """
    Class representing an API request with decorators.
    """
    
    def __init__(
        self,
        prompt: str,
        decorators: Optional[List[BaseDecorator]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize an API request.
        
        Args:
            prompt: The prompt text.
            decorators: Optional list of decorators to apply.
            metadata: Optional metadata for the request.
        """
        self.prompt = prompt
        self.decorators = decorators or []
        self.metadata = metadata or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the API request to a dictionary.
        
        Returns:
            A dictionary representation of the API request.
        """
        return {
            "prompt": self.prompt,
            "decorators": [d.to_dict() for d in self.decorators],
            "metadata": self.metadata
        }
    
    def to_json(self) -> str:
        """
        Convert the API request to a JSON string.
        
        Returns:
            A JSON string representation of the API request.
        """
        return json.dumps(self.to_dict(), indent=2)
    
    def to_decorated_prompt(self) -> str:
        """
        Convert the API request to a decorated prompt string.
        
        Returns:
            A decorated prompt string.
        """
        return apply_decorators(self.decorators, self.prompt)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'APIRequest':
        """
        Create an API request from a dictionary.
        
        Args:
            data: The dictionary to create the API request from.
            
        Returns:
            An API request object.
        """
        prompt = data.get("prompt", "")
        metadata = data.get("metadata", {})
        
        decorators = []
        for decorator_dict in data.get("decorators", []):
            name = decorator_dict.get("name", "")
            version = decorator_dict.get("version", "1.0.0")
            parameters = decorator_dict.get("parameters", {})
            metadata = decorator_dict.get("metadata", {})
            
            if name == "Reasoning":
                depth = parameters.get("depth", ReasoningDepth.MODERATE)
                decorators.append(Reasoning(depth=depth, metadata=metadata))
            elif name == "StepByStep":
                numbered = parameters.get("numbered", True)
                decorators.append(StepByStep(numbered=numbered, metadata=metadata))
            elif name == "OutputFormat":
                format_value = parameters.get("format", OutputFormatType.PLAINTEXT)
                decorators.append(OutputFormat(format=format_value, metadata=metadata))
            elif name == "Tone":
                style = parameters.get("style", ToneStyle.FORMAL)
                decorators.append(Tone(style=style, metadata=metadata))
            elif name == "Version":
                standard = parameters.get("standard", "1.0.0")
                decorators.append(Version(standard=standard, metadata=metadata))
            else:
                decorators.append(BaseDecorator(name=name, version=version, parameters=parameters, metadata=metadata))
        
        return cls(prompt=prompt, decorators=decorators, metadata=metadata)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'APIRequest':
        """
        Create an API request from a JSON string.
        
        Args:
            json_str: The JSON string to create the API request from.
            
        Returns:
            An API request object.
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    @classmethod
    def from_decorated_prompt(cls, decorated_prompt: str) -> 'APIRequest':
        """
        Create an API request from a decorated prompt string.
        
        Args:
            decorated_prompt: The decorated prompt string to create the API request from.
            
        Returns:
            An API request object.
        """
        lines = decorated_prompt.strip().split("\n")
        
        decorators = []
        prompt_lines = []
        
        for line in lines:
            line = line.strip()
            if line.startswith("+++"):
                decorator = parse_decorator_string(line)
                if decorator:
                    decorators.append(decorator)
            else:
                # If we've already seen a non-decorator line, all subsequent lines are part of the prompt
                if prompt_lines or not line.startswith("+++"):
                    prompt_lines.append(line)
        
        prompt = "\n".join(prompt_lines).strip()
        return cls(prompt=prompt, decorators=decorators)


def main():
    """Example usage of the Prompt Decorators Core extension package."""
    # Create decorators
    reasoning = Reasoning(depth=ReasoningDepth.COMPREHENSIVE)
    step_by_step = StepByStep(numbered=True)
    output_format = OutputFormat(format=OutputFormatType.MARKDOWN)
    tone = Tone(style=ToneStyle.TECHNICAL)
    
    # Create an API request
    request = APIRequest(
        prompt="Explain how nuclear fusion works",
        decorators=[reasoning, step_by_step, output_format, tone]
    )
    
    # Print the decorated prompt
    print("Decorated Prompt:")
    print(request.to_decorated_prompt())
    print()
    
    # Print the JSON representation
    print("JSON Representation:")
    print(request.to_json())
    print()
    
    # Print the system instructions
    print("System Instructions:")
    print(convert_decorators_to_system_instructions(request.decorators))
    print()
    
    # Parse a decorated prompt
    decorated_prompt = """+++Reasoning(depth=comprehensive)
+++StepByStep(numbered=true)
+++OutputFormat(format=json)
What factors should I consider when choosing a programming language for a new project?"""
    
    parsed_request = APIRequest.from_decorated_prompt(decorated_prompt)
    
    print("Parsed Decorated Prompt:")
    print(decorated_prompt)
    print()
    
    print("Parsed Decorators:")
    for decorator in parsed_request.decorators:
        print(f"- {decorator.to_string()}")
    print()
    
    print("Parsed Prompt:")
    print(parsed_request.prompt)


if __name__ == "__main__":
    main() 