"""Tests for the OutputFormat decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.output_format import OutputFormat


class TestOutputFormat(unittest.TestCase):
    """Tests for the OutputFormat decorator.

    Specifies the format of the AI's response. This decorator ensures the output
    follows a specific format, making it easier to parse, display, or process
    the response in a consistent way.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "format": "json",
        }

    def test_missing_required_param_format(self):
        """Test that initialization fails when missing required parameter format."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "format" in params:
            del params["format"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            OutputFormat(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "format" in error_message or "required" in error_message.lower()
        )

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["format"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            OutputFormat(**params)
        self.assertIn("format", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["format"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            OutputFormat(**params)
        self.assertIn("format", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["format"] = "json"
        # This should not raise an exception
        OutputFormat(**params)
        params["format"] = "markdown"
        # This should not raise an exception
        OutputFormat(**params)
        params["format"] = "yaml"
        # This should not raise an exception
        OutputFormat(**params)
        params["format"] = "xml"
        # This should not raise an exception
        OutputFormat(**params)
        params["format"] = "plaintext"
        # This should not raise an exception
        OutputFormat(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # JSON output for structured data
        params = self._get_valid_params()
        decorator = OutputFormat(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Markdown output for formatted text
        params = self._get_valid_params()
        decorator = OutputFormat(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = OutputFormat(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "output_format")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = OutputFormat.from_dict(serialized)
        self.assertIsInstance(deserialized, OutputFormat)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
