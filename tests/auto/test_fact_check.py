"""Tests for the FactCheck decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.fact_check import FactCheck


class TestFactCheck(unittest.TestCase):
    """Tests for the FactCheck decorator.

    Enhances the response with verification of factual claims and explicit
    indication of confidence levels. This decorator promotes accuracy by
    distinguishing between well-established facts, likely facts, and uncertain
    or speculative information.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "confidence": True,
            "uncertain": "mark",
            "strictness": "low",
        }

    def test_validate_confidence(self):
        """Test validation for the confidence parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["confidence"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            FactCheck(**params)
        self.assertIn("confidence", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_uncertain(self):
        """Test validation for the uncertain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["uncertain"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            FactCheck(**params)
        self.assertIn("uncertain", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["uncertain"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            FactCheck(**params)
        self.assertIn("uncertain", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["uncertain"] = "mark"
        # This should not raise an exception
        FactCheck(**params)
        params["uncertain"] = "exclude"
        # This should not raise an exception
        FactCheck(**params)
        params["uncertain"] = "qualify"
        # This should not raise an exception
        FactCheck(**params)

    def test_validate_strictness(self):
        """Test validation for the strictness parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["strictness"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            FactCheck(**params)
        self.assertIn("strictness", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["strictness"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            FactCheck(**params)
        self.assertIn("strictness", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["strictness"] = "low"
        # This should not raise an exception
        FactCheck(**params)
        params["strictness"] = "moderate"
        # This should not raise an exception
        FactCheck(**params)
        params["strictness"] = "high"
        # This should not raise an exception
        FactCheck(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic fact checking with confidence indicators
        params = self._get_valid_params()
        decorator = FactCheck(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # High-strictness fact checking that excludes uncertain information
        params = self._get_valid_params()
        decorator = FactCheck(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = FactCheck(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "fact_check")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = FactCheck.from_dict(serialized)
        self.assertIsInstance(deserialized, FactCheck)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
