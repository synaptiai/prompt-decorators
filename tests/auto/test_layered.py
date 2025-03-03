"""Tests for the Layered decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.layered import Layered


class TestLayered(unittest.TestCase):
    """Tests for the Layered decorator.

    Presents content at multiple levels of explanation depth, allowing readers
    to engage with information at their preferred level of detail. This
    decorator structures responses with progressive disclosure, from high-level
    summaries to increasingly detailed explanations.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "levels": "sentence-paragraph-full",
            "count": 3,
            "progression": "separate",
        }

    def test_validate_levels(self):
        """Test validation for the levels parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["levels"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("levels", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["levels"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("levels", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["levels"] = "sentence-paragraph-full"
        # This should not raise an exception
        Layered(**params)
        params["levels"] = "basic-intermediate-advanced"
        # This should not raise an exception
        Layered(**params)
        params["levels"] = "summary-detail-technical"
        # This should not raise an exception
        Layered(**params)

    def test_validate_count(self):
        """Test validation for the count parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["count"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("count", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["count"] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["count"] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_progression(self):
        """Test validation for the progression parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["progression"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("progression", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["progression"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Layered(**params)
        self.assertIn("progression", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["progression"] = "separate"
        # This should not raise an exception
        Layered(**params)
        params["progression"] = "nested"
        # This should not raise an exception
        Layered(**params)
        params["progression"] = "incremental"
        # This should not raise an exception
        Layered(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic three-level explanation of a complex concept
        params = self._get_valid_params()
        decorator = Layered(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Multi-layered nested progression with custom levels
        params = self._get_valid_params()
        decorator = Layered(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Layered(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "layered")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Layered.from_dict(serialized)
        self.assertIsInstance(deserialized, Layered)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
