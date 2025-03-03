"""Tests for the Audience decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.audience import Audience


class TestAudience(unittest.TestCase):
    """Tests for the Audience decorator.

    Adapts the response for a specific audience expertise level. This decorator
    ensures content is appropriately tailored to the knowledge, vocabulary, and
    needs of different audience types, from beginners to technical experts.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "level": "beginner",
            "domain": "general",
            "examples": True,
        }

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["level"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Audience(**params)
        self.assertIn("level", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["level"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Audience(**params)
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
        Audience(**params)
        params["level"] = "intermediate"
        # This should not raise an exception
        Audience(**params)
        params["level"] = "expert"
        # This should not raise an exception
        Audience(**params)
        params["level"] = "technical"
        # This should not raise an exception
        Audience(**params)

    def test_validate_domain(self):
        """Test validation for the domain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["domain"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Audience(**params)
        self.assertIn("domain", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_examples(self):
        """Test validation for the examples parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["examples"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Audience(**params)
        self.assertIn("examples", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Technical explanation for experts in a specific field
        params = self._get_valid_params()
        decorator = Audience(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Beginner-friendly explanation with examples
        params = self._get_valid_params()
        decorator = Audience(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Audience(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "audience")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Audience.from_dict(serialized)
        self.assertIsInstance(deserialized, Audience)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
