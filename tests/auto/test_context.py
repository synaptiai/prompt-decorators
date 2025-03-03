"""Tests for the Context decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.context import Context


class TestContext(unittest.TestCase):
    """Tests for the Context decorator.

    A meta-decorator that adapts standard decorators for domain-specific
    contexts. This provides specialized interpretations of decorators based on
    particular fields, industries, or subject matter to ensure appropriate
    adaptation to contextual requirements.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "domain": "example_value",
            "scope": "terminology",
            "level": "beginner",
        }

    def test_missing_required_param_domain(self):
        """Test that initialization fails when missing required parameter domain."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "domain" in params:
            del params["domain"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Context(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "domain" in error_message or "required" in error_message.lower()
        )

    def test_validate_domain(self):
        """Test validation for the domain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["domain"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Context(**params)
        self.assertIn("domain", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_scope(self):
        """Test validation for the scope parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["scope"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Context(**params)
        self.assertIn("scope", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["scope"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Context(**params)
        self.assertIn("scope", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["scope"] = "terminology"
        # This should not raise an exception
        Context(**params)
        params["scope"] = "examples"
        # This should not raise an exception
        Context(**params)
        params["scope"] = "structure"
        # This should not raise an exception
        Context(**params)
        params["scope"] = "all"
        # This should not raise an exception
        Context(**params)

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["level"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Context(**params)
        self.assertIn("level", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["level"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Context(**params)
        self.assertIn("level", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["level"] = "beginner"
        # This should not raise an exception
        Context(**params)
        params["level"] = "intermediate"
        # This should not raise an exception
        Context(**params)
        params["level"] = "expert"
        # This should not raise an exception
        Context(**params)
        params["level"] = "mixed"
        # This should not raise an exception
        Context(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic domain-specific adaptation of decorators
        params = self._get_valid_params()
        decorator = Context(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Targeted contextualization for specific expertise level
        params = self._get_valid_params()
        decorator = Context(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Context(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "context")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Context.from_dict(serialized)
        self.assertIsInstance(deserialized, Context)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
