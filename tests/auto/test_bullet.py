"""Tests for the Bullet decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.bullet import Bullet


class TestBullet(unittest.TestCase):
    """Tests for the Bullet decorator.

    Formats the response as a bulleted list, making information easier to scan
    and digest. This decorator is ideal for presenting sequential steps, key
    points, or collections of related items in a clean, concise format.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "style": "dash",
            "indented": True,
            "compact": False,
        }

    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["style"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Bullet(**params)
        self.assertIn("style", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["style"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Bullet(**params)
        self.assertIn("style", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["style"] = "dash"
        # This should not raise an exception
        Bullet(**params)
        params["style"] = "dot"
        # This should not raise an exception
        Bullet(**params)
        params["style"] = "arrow"
        # This should not raise an exception
        Bullet(**params)
        params["style"] = "star"
        # This should not raise an exception
        Bullet(**params)
        params["style"] = "plus"
        # This should not raise an exception
        Bullet(**params)

    def test_validate_indented(self):
        """Test validation for the indented parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["indented"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Bullet(**params)
        self.assertIn("indented", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_compact(self):
        """Test validation for the compact parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["compact"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Bullet(**params)
        self.assertIn("compact", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic bulleted list of key points
        params = self._get_valid_params()
        decorator = Bullet(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Compact star bullets with nesting disabled
        params = self._get_valid_params()
        decorator = Bullet(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Bullet(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "bullet")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Bullet.from_dict(serialized)
        self.assertIsInstance(deserialized, Bullet)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
