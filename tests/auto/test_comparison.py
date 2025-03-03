"""Tests for the Comparison decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.comparison import Comparison


class TestComparison(unittest.TestCase):
    """Tests for the Comparison decorator.

    Structures the response as a direct comparison between multiple items,
    concepts, or approaches. This decorator is ideal for highlighting
    similarities and differences across specific dimensions or criteria.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "aspects": [],
            "format": "table",
            "highlight": True,
        }

    def test_validate_aspects(self):
        """Test validation for the aspects parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["aspects"] = "not_an_array"  # Not an array
        with self.assertRaises(ValidationError) as context:
            Comparison(**params)
        self.assertIn("aspects", str(context.exception))
        self.assertIn("array", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["format"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Comparison(**params)
        self.assertIn("format", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["format"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Comparison(**params)
        self.assertIn("format", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["format"] = "table"
        # This should not raise an exception
        Comparison(**params)
        params["format"] = "prose"
        # This should not raise an exception
        Comparison(**params)
        params["format"] = "bullets"
        # This should not raise an exception
        Comparison(**params)

    def test_validate_highlight(self):
        """Test validation for the highlight parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["highlight"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Comparison(**params)
        self.assertIn("highlight", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic tabular comparison of specific aspects
        params = self._get_valid_params()
        decorator = Comparison(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Prose-based comparison without specific aspects
        params = self._get_valid_params()
        decorator = Comparison(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Comparison(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "comparison")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Comparison.from_dict(serialized)
        self.assertIsInstance(deserialized, Comparison)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
