"""Tests for the Confidence decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.confidence import Confidence


class TestConfidence(unittest.TestCase):
    """Tests for the Confidence decorator.

    Enhances the response with explicit indications of confidence levels for
    different statements or claims. This decorator promotes transparency about
    knowledge certainty and helps differentiate between well-established facts
    and more speculative content.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "scale": "percent",
            "threshold": 50,
            "detailed": False,
        }

    def test_validate_scale(self):
        """Test validation for the scale parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["scale"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("scale", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["scale"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("scale", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["scale"] = "percent"
        # This should not raise an exception
        Confidence(**params)
        params["scale"] = "qualitative"
        # This should not raise an exception
        Confidence(**params)
        params["scale"] = "stars"
        # This should not raise an exception
        Confidence(**params)
        params["scale"] = "numeric"
        # This should not raise an exception
        Confidence(**params)

    def test_validate_threshold(self):
        """Test validation for the threshold parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["threshold"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("threshold", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["threshold"] = -1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("threshold", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["threshold"] = 101  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("threshold", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_detailed(self):
        """Test validation for the detailed parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["detailed"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Confidence(**params)
        self.assertIn("detailed", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Qualitative confidence indicators for a complex topic
        params = self._get_valid_params()
        decorator = Confidence(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed percentage-based confidence with high threshold
        params = self._get_valid_params()
        decorator = Confidence(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Confidence(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "confidence")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Confidence.from_dict(serialized)
        self.assertIsInstance(deserialized, Confidence)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
