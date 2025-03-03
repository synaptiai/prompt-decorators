"""Tests for the Prioritize decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.prioritize import Prioritize


class TestPrioritize(unittest.TestCase):
    """Tests for the Prioritize decorator.

    Structures the response by ranking information according to importance,
    urgency, or impact. This decorator helps identify the most critical aspects
    of a topic and presents information in a hierarchical manner from most to
    least important.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "criteria": "importance",
            "count": 5,
            "showRationale": False,
        }

    def test_validate_criteria(self):
        """Test validation for the criteria parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["criteria"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Prioritize(**params)
        self.assertIn("criteria", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_count(self):
        """Test validation for the count parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["count"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Prioritize(**params)
        self.assertIn("count", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["count"] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Prioritize(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["count"] = 11  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Prioritize(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_showRationale(self):
        """Test validation for the showRationale parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["showRationale"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Prioritize(**params)
        self.assertIn("showRationale", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic prioritization of key factors
        params = self._get_valid_params()
        decorator = Prioritize(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed prioritization with custom criteria and rationale
        params = self._get_valid_params()
        decorator = Prioritize(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Prioritize(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "prioritize")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Prioritize.from_dict(serialized)
        self.assertIsInstance(deserialized, Prioritize)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
