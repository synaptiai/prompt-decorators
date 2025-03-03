"""Tests for the StyleShift decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.style_shift import StyleShift


class TestStyleShift(unittest.TestCase):
    """Tests for the StyleShift decorator.

    Modifies specific style characteristics of responses such as formality,
    persuasiveness, or urgency. This decorator enables fine-tuned control over
    particular aspects of communication style without changing the overall tone.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "aspect": "formality",
            "level": 3,
            "maintain": [],
        }

    def test_missing_required_param_aspect(self):
        """Test that initialization fails when missing required parameter aspect."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "aspect" in params:
            del params["aspect"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            StyleShift(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "aspect" in error_message or "required" in error_message.lower()
        )

    def test_validate_aspect(self):
        """Test validation for the aspect parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["aspect"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("aspect", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["aspect"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("aspect", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["aspect"] = "formality"
        # This should not raise an exception
        StyleShift(**params)
        params["aspect"] = "persuasion"
        # This should not raise an exception
        StyleShift(**params)
        params["aspect"] = "urgency"
        # This should not raise an exception
        StyleShift(**params)
        params["aspect"] = "confidence"
        # This should not raise an exception
        StyleShift(**params)
        params["aspect"] = "complexity"
        # This should not raise an exception
        StyleShift(**params)

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["level"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("level", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["level"] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("level", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["level"] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("level", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_maintain(self):
        """Test validation for the maintain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["maintain"] = "not_an_array"  # Not an array
        with self.assertRaises(ValidationError) as context:
            StyleShift(**params)
        self.assertIn("maintain", str(context.exception))
        self.assertIn("array", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Highly formal style while maintaining normal complexity
        params = self._get_valid_params()
        decorator = StyleShift(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Increased urgency for a business communication
        params = self._get_valid_params()
        decorator = StyleShift(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = StyleShift(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "style_shift")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = StyleShift.from_dict(serialized)
        self.assertIsInstance(deserialized, StyleShift)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
