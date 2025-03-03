"""Tests for the Constraints decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.constraints import Constraints


class TestConstraints(unittest.TestCase):
    """Tests for the Constraints decorator.

    Applies specific limitations to the output format, length, or content. This
    decorator enforces creative constraints that can enhance focus, brevity, or
    precision by requiring the response to work within defined boundaries.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "wordCount": 11,
            "timeframe": "example_value",
            "vocabulary": "simple",
            "custom": "example_value",
        }

    def test_validate_wordCount(self):
        """Test validation for the wordCount parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["wordCount"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("wordCount", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["wordCount"] = 9  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("wordCount", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["wordCount"] = 1001  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("wordCount", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_timeframe(self):
        """Test validation for the timeframe parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["timeframe"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("timeframe", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_vocabulary(self):
        """Test validation for the vocabulary parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["vocabulary"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("vocabulary", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["vocabulary"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("vocabulary", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["vocabulary"] = "simple"
        # This should not raise an exception
        Constraints(**params)
        params["vocabulary"] = "technical"
        # This should not raise an exception
        Constraints(**params)
        params["vocabulary"] = "domain-specific"
        # This should not raise an exception
        Constraints(**params)
        params["vocabulary"] = "creative"
        # This should not raise an exception
        Constraints(**params)

    def test_validate_custom(self):
        """Test validation for the custom parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["custom"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Constraints(**params)
        self.assertIn("custom", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Word count constraint for a complex topic
        params = self._get_valid_params()
        decorator = Constraints(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Multiple constraints for a creative response
        params = self._get_valid_params()
        decorator = Constraints(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Constraints(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "constraints")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Constraints.from_dict(serialized)
        self.assertIsInstance(deserialized, Constraints)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
