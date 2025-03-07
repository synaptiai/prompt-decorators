#!/usr/bin/env python
"""Debug script for testing the transform function in DynamicDecorator.

This script provides a way to test the transform function in isolation,
which is useful for debugging issues with the transformation logic.
"""

import logging
import sys
from typing import Any, Callable, Dict, cast

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("debug_transform")


def test_decorator_transform():
    """Test decorator with a transform function."""
    return """
result = "This is a test transformation.\\n"
result += f"Parameter value: {kwargs.get('param1', 'default')}\\n"
return result + text
    """


def step_by_step_transform():
    """StepByStep decorator transform function."""
    return """
result = "Please break down your response into clear, sequential steps.\\n"
if kwargs.get("numbered", True):
    result += "Number each step sequentially (Step 1, Step 2, etc.).\\n"
else:
    result += "Use bullet points for each step instead of numbers.\\n"
return result + text
    """


def debug_transform_function(
    transform_function: str, text: str, parameters: Dict[str, Any]
) -> str:
    """Debug the transform function.

    Args:
        transform_function: The transform function code
        text: The text to transform
        parameters: The parameters to use

    Returns:
        The transformed text
    """
    logger.debug(f"Transform function: {transform_function}")
    logger.debug(f"Text: {text}")
    logger.debug(f"Parameters: {parameters}")

    try:
        # Create a Python function from the transform function
        transform_code = f"def transform(text, **kwargs):\n"
        for line in transform_function.split("\n"):
            transform_code += f"    {line}\n"

        logger.debug(f"Transform code:\n{transform_code}")

        # Compile and execute the function
        namespace: Dict[str, Any] = {}
        exec(transform_code, namespace)
        transform = namespace["transform"]

        # Call the function with the text and parameters
        # Pass parameters as kwargs, not as a second positional argument
        result = transform(text, **parameters)

        # Ensure the result is a string
        if not isinstance(result, str):
            result = str(result)

        logger.debug(f"Result: {result}")
        return cast(str, result)
    except Exception as e:
        logger.error(f"Error applying transform function: {e}")
        import traceback

        traceback.print_exc()
        return text


def main():
    """Run the debug script."""
    logger.info("=== Testing basic transform function ===")
    text = "This is a test prompt."
    parameters = {"param1": "test_value"}
    transform_function = test_decorator_transform()

    transformed = debug_transform_function(transform_function, text, parameters)
    print("\nTransformed text:")
    print(transformed)

    logger.info("=== Testing StepByStep transform function ===")
    parameters = {"numbered": True}
    transform_function = step_by_step_transform()

    transformed = debug_transform_function(transform_function, text, parameters)
    print("\nTransformed text (StepByStep):")
    print(transformed)


if __name__ == "__main__":
    main()
