"""Tests for the Tone decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.tone import Tone


class TestTone(unittest.TestCase):
    """Tests for the Tone decorator.

    Adjusts the writing style and tone of the AI's response. This decorator
    helps ensure that responses are appropriately styled for different audiences
    and contexts, from formal technical documentation to casual explanations.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "style": "formal",
        }

    def test_missing_required_param_style(self):
        """Test that initialization fails when missing required parameter style."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "style" in params:
            del params["style"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Tone(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue("style" in error_message or "required" in error_message.lower())

    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["style"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Tone(**params)
        self.assertIn("style", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["style"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Tone(**params)
        self.assertIn("style", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["style"] = "formal"
        # This should not raise an exception
        Tone(**params)
        params["style"] = "casual"
        # This should not raise an exception
        Tone(**params)
        params["style"] = "friendly"
        # This should not raise an exception
        Tone(**params)
        params["style"] = "technical"
        # This should not raise an exception
        Tone(**params)
        params["style"] = "humorous"
        # This should not raise an exception
        Tone(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Technical documentation tone
        params = self._get_valid_params()
        decorator = Tone(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Casual explanation
        params = self._get_valid_params()
        decorator = Tone(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Tone(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "tone")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Tone.from_dict(serialized)
        self.assertIsInstance(deserialized, Tone)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
