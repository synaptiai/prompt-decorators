"""Tests for the Override decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.override import Override


class TestOverride(unittest.TestCase):
    """Tests for the Override decorator.

    A meta-decorator that overrides the default parameters or behaviors of other
    decorators. This enables customization of standard decorators without
    modifying their definitions, allowing for reuse of established patterns with
    specific adjustments.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "decorator": "example_value",
            "parameters": "example_value",
            "behavior": "example_value",
        }

    def test_missing_required_param_decorator(self):
        """Test that initialization fails when missing required parameter decorator."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "decorator" in params:
            del params["decorator"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Override(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "decorator" in error_message or "required" in error_message.lower()
        )

    def test_validate_decorator(self):
        """Test validation for the decorator parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["decorator"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Override(**params)
        self.assertIn("decorator", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_parameters(self):
        """Test validation for the parameters parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["parameters"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Override(**params)
        self.assertIn("parameters", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_behavior(self):
        """Test validation for the behavior parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["behavior"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Override(**params)
        self.assertIn("behavior", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic parameter override for a standard decorator
        params = self._get_valid_params()
        decorator = Override(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Complex behavior override with custom instructions
        params = self._get_valid_params()
        decorator = Override(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Override(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "override")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Override.from_dict(serialized)
        self.assertIsInstance(deserialized, Override)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
