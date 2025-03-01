"""
Utility functions for the Prompt Decorators Core extension package.
"""

import re
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union


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
        return f'"{value.value}"'
    elif isinstance(value, str):
        return f'"{value}"'
    else:
        return str(value)


def parse_decorated_prompt(text: str) -> Tuple[List[Dict[str, Any]], str]:
    """
    Parse a decorated prompt into a list of decorators and the prompt text.
    
    Args:
        text: The decorated prompt text.
        
    Returns:
        A tuple containing a list of decorator dictionaries and the prompt text.
    """
    # Regular expression to match decorators
    decorator_pattern = r'\+\+\+(\w+)\((.*?)\)'
    
    # Find all decorators in the text
    decorators = []
    for match in re.finditer(decorator_pattern, text):
        name = match.group(1)
        params_str = match.group(2)
        
        # Parse parameters
        parameters = {}
        if params_str.strip():
            param_pattern = r'(\w+)=(?:"([^"]*)"|(true|false)|(\d+(?:\.\d+)?))'
            for param_match in re.finditer(param_pattern, params_str):
                param_name = param_match.group(1)
                # Check which group matched (string, boolean, or number)
                if param_match.group(2) is not None:
                    param_value = param_match.group(2)  # String value
                elif param_match.group(3) is not None:
                    param_value = param_match.group(3) == 'true'  # Boolean value
                else:
                    # Number value - convert to int if it's an integer, float otherwise
                    num_str = param_match.group(4)
                    param_value = int(num_str) if num_str.isdigit() else float(num_str)
                
                parameters[param_name] = param_value
        
        decorators.append({
            "name": name,
            "version": "1.0.0",  # Default version
            "parameters": parameters,
            "metadata": {"category": "core"}  # Default metadata
        })
    
    # Remove decorators from the text to get the prompt
    prompt = re.sub(decorator_pattern, '', text).strip()
    
    return decorators, prompt


def generate_system_instructions(decorators: List[Dict[str, Any]]) -> str:
    """
    Generate system instructions based on the decorators.
    
    Args:
        decorators: A list of decorator dictionaries.
        
    Returns:
        A string containing system instructions.
    """
    instructions = []
    
    for decorator in decorators:
        name = decorator["name"]
        params = decorator["parameters"]
        
        if name == "Reasoning":
            depth = params.get("depth", "moderate")
            depth_instructions = {
                "basic": "Show basic reasoning in your response.",
                "moderate": "Show your step-by-step reasoning process in moderate detail.",
                "comprehensive": "Provide comprehensive reasoning, exploring multiple perspectives and trade-offs."
            }
            instructions.append(depth_instructions.get(depth, depth_instructions["moderate"]))
        
        elif name == "StepByStep":
            numbered = params.get("numbered", True)
            if numbered:
                instructions.append("Break down your response into numbered steps.")
            else:
                instructions.append("Break down your response into clear steps.")
        
        elif name == "OutputFormat":
            format_type = params.get("format", "plaintext")
            format_instructions = {
                "plaintext": "Format your response as plain text.",
                "markdown": "Format your response using Markdown syntax.",
                "json": "Format your response as a valid JSON object.",
                "yaml": "Format your response as valid YAML.",
                "xml": "Format your response as valid XML."
            }
            instructions.append(format_instructions.get(format_type, format_instructions["plaintext"]))
        
        elif name == "Tone":
            style = params.get("style", "formal")
            style_instructions = {
                "formal": "Use a formal, professional tone in your response.",
                "casual": "Use a casual, conversational tone in your response.",
                "friendly": "Use a friendly, approachable tone in your response.",
                "technical": "Use a technical, precise tone with appropriate terminology.",
                "humorous": "Include appropriate humor in your response."
            }
            instructions.append(style_instructions.get(style, style_instructions["formal"]))
    
    return "\n".join(instructions) 