"""Tests for the Alternatives decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.alternatives import Alternatives


class TestAlternatives(unittest.TestCase):
    """Tests for the Alternatives decorator.

    Presents multiple distinct options, approaches, or solutions to a question
    or problem. This decorator encourages exploring different paths or
    perspectives rather than providing a single definitive answer.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "count": 3,
            "diversity": "low",
            "comparison": False,
        }

    def test_validate_count(self):
        """Test validation for the count parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["count"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("count", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["count"] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["count"] = 8  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_diversity(self):
        """Test validation for the diversity parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["diversity"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("diversity", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["diversity"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("diversity", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["diversity"] = "low"
        # This should not raise an exception
        Alternatives(**params)
        params["diversity"] = "medium"
        # This should not raise an exception
        Alternatives(**params)
        params["diversity"] = "high"
        # This should not raise an exception
        Alternatives(**params)

    def test_validate_comparison(self):
        """Test validation for the comparison parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["comparison"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Alternatives(**params)
        self.assertIn("comparison", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic alternative approaches to a problem
        params = self._get_valid_params()
        decorator = Alternatives(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Highly diverse alternatives with comparative analysis
        params = self._get_valid_params()
        decorator = Alternatives(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Alternatives(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "alternatives")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Alternatives.from_dict(serialized)
        self.assertIsInstance(deserialized, Alternatives)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
