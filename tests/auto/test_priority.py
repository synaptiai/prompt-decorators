"""Tests for the Priority decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.priority import Priority


class TestPriority(unittest.TestCase):
    """Tests for the Priority decorator.

    A meta-decorator that establishes a precedence hierarchy among multiple
    decorators. This allows explicit control over which decorator's parameters
    or behaviors take precedence when conflicts arise, overriding the default
    last-decorator-wins behavior.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "decorators": [],
            "explicit": False,
            "mode": "override",
        }

    def test_missing_required_param_decorators(self):
        """Test that initialization fails when missing required parameter decorators."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "decorators" in params:
            del params["decorators"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Priority(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "decorators" in error_message or "required" in error_message.lower()
        )

    def test_validate_decorators(self):
        """Test validation for the decorators parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["decorators"] = "not_an_array"  # Not an array
        with self.assertRaises(ValidationError) as context:
            Priority(**params)
        self.assertIn("decorators", str(context.exception))
        self.assertIn("array", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_explicit(self):
        """Test validation for the explicit parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["explicit"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Priority(**params)
        self.assertIn("explicit", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_mode(self):
        """Test validation for the mode parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["mode"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Priority(**params)
        self.assertIn("mode", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["mode"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Priority(**params)
        self.assertIn("mode", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["mode"] = "override"
        # This should not raise an exception
        Priority(**params)
        params["mode"] = "merge"
        # This should not raise an exception
        Priority(**params)
        params["mode"] = "cascade"
        # This should not raise an exception
        Priority(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic priority ordering between potentially conflicting decorators
        params = self._get_valid_params()
        decorator = Priority(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Complex priority with explicit conflict resolution
        params = self._get_valid_params()
        decorator = Priority(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Priority(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "priority")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Priority.from_dict(serialized)
        self.assertIsInstance(deserialized, Priority)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
