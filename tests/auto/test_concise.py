"""Tests for the Concise decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.concise import Concise


class TestConcise(unittest.TestCase):
    """Tests for the Concise decorator.

    Optimizes the response for brevity and directness, eliminating unnecessary
    details and verbose language. This decorator is ideal for obtaining quick
    answers, executive summaries, or essential information when time or space is
    limited.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "maxWords": 11,
            "bulletPoints": False,
            "level": "moderate",
        }

    def test_validate_maxWords(self):
        """Test validation for the maxWords parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["maxWords"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("maxWords", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["maxWords"] = 9  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("maxWords", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["maxWords"] = 501  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("maxWords", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_bulletPoints(self):
        """Test validation for the bulletPoints parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["bulletPoints"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("bulletPoints", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["level"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("level", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["level"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Concise(**params)
        self.assertIn("level", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["level"] = "moderate"
        # This should not raise an exception
        Concise(**params)
        params["level"] = "high"
        # This should not raise an exception
        Concise(**params)
        params["level"] = "extreme"
        # This should not raise an exception
        Concise(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic concise explanation of a complex topic
        params = self._get_valid_params()
        decorator = Concise(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Extremely concise bulleted answer with word limit
        params = self._get_valid_params()
        decorator = Concise(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Concise(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "concise")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Concise.from_dict(serialized)
        self.assertIsInstance(deserialized, Concise)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
