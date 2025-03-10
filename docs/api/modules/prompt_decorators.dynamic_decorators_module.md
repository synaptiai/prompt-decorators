# prompt_decorators.dynamic_decorators_module

Dynamic Prompt Decorators Module.

This module provides a unified interface for working with prompt decorators
without the need for code generation. It dynamically loads decorator definitions
from the registry at runtime, removing the need to generate Python classes for
each decorator.

Features:
- Dynamic loading of decorators from registry
- Prompt transformation with any decorator
- Parameter validation against schema
- Support for decorator composition

## Classes

### DecoratorDefinition

Class representing a decorator definition.

#### Methods

##### `__init__`

Initialize a decorator definition.

        Args:
            name: Name of the decorator
            description: Description of the decorator
            category: Category of the decorator
            parameters: List of parameter definitions
            transform_function: JavaScript function for transforming prompts
            version: Version of the decorator

##### `to_dict`

Convert the definition to a dictionary.

## Functions

### apply_decorator

Apply a decorator to a prompt.

    Args:
        decorator_name: Name of the decorator
        prompt: The prompt text
        **kwargs: Parameters for the decorator

    Returns:
        The transformed prompt

#### Parameters

- `decorator_name`: str
- `prompt`: str
- `kwargs`: Any

### apply_dynamic_decorators

Apply decorators to a prompt using the +++ syntax.

    Args:
        prompt: The prompt text with decorator syntax

    Returns:
        The transformed prompt

#### Parameters

- `prompt`: str

### create_decorator

Create a decorator instance by name (alias for create_decorator_instance).

    This function is maintained for backward compatibility with demo code.

    Args:
        name: Name of the decorator
        **kwargs: Parameters for the decorator

    Returns:
        A decorator instance

    Raises:
        ValueError: If the decorator is not found

#### Parameters

- `name`: str
- `kwargs`: Any

### create_decorator_class

Create a decorator class from a definition.

    Args:
        definition: Decorator definition

    Returns:
        A decorator class

#### Parameters

- `definition`: DecoratorDefinition

### create_decorator_instance

Create a decorator instance by name.

    Args:
        name: Name of the decorator
        **kwargs: Parameters for the decorator

    Returns:
        A decorator instance

    Raises:
        ValueError: If the decorator is not found

#### Parameters

- `name`: str
- `kwargs`: Any

### extract_decorator_name

Extract the decorator name from decorator text.

    Args:
        decorator_text: Text containing a decorator definition

    Returns:
        The decorator name

#### Parameters

- `decorator_text`: str

### get_available_decorators

Get a list of all available decorators.

    Returns:
        List of decorator definitions

### list_available_decorators

List all available decorator names.

    This function is maintained for backward compatibility with demo code.

    Returns:
        A list of decorator names

### load_decorator_definitions

Load decorator definitions from the registry.

### parse_decorator_text

Parse decorator text into name and parameters.

    Args:
        decorator_text: Text containing a decorator definition

    Returns:
        Tuple of (name, parameters)

#### Parameters

- `decorator_text`: str

### register_decorator

Register a decorator definition.

    Args:
        definition: Decorator definition

    Returns:
        None

#### Parameters

- `definition`: DecoratorDefinition

### transform_prompt

Transform a prompt using a list of decorator strings.

    This function is a wrapper around the core transform_prompt function
    to ensure backward compatibility with the demo.

    Args:
        prompt: The prompt to transform
        decorators: List of decorator strings

    Returns:
        The transformed prompt

#### Parameters

- `prompt`: str
- `decorators`: List
