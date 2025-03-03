"""Tests for the Debate decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.debate import Debate


class TestDebate(unittest.TestCase):
    """Tests for the Debate decorator.

    Structures the response as a debate between multiple perspectives on a
    topic. This decorator encourages balanced representation of different
    viewpoints and helps explore complex issues from various angles.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "perspectives": 2,
            "balanced": True,
        }

    def test_validate_perspectives(self):
        """Test validation for the perspectives parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["perspectives"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Debate(**params)
        self.assertIn("perspectives", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["perspectives"] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Debate(**params)
        self.assertIn("perspectives", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["perspectives"] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Debate(**params)
        self.assertIn("perspectives", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_balanced(self):
        """Test validation for the balanced parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["balanced"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Debate(**params)
        self.assertIn("balanced", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Two-perspective debate on an ethical issue
        params = self._get_valid_params()
        decorator = Debate(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Three-perspective debate on a policy issue with balanced representation
        params = self._get_valid_params()
        decorator = Debate(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Debate(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "debate")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Debate.from_dict(serialized)
        self.assertIsInstance(deserialized, Debate)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
