"""Tests for the StepByStep decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.step_by_step import StepByStep


class TestStepByStep(unittest.TestCase):
    """Tests for the StepByStep decorator.

    Structures the AI's response as a sequence of clearly labeled steps. This
    decorator helps break down complex processes, explanations, or solutions
    into manageable, sequential parts for better understanding.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "numbered": True,
        }

    def test_validate_numbered(self):
        """Test validation for the numbered parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["numbered"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            StepByStep(**params)
        self.assertIn("numbered", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Numbered steps for a technical process
        params = self._get_valid_params()
        decorator = StepByStep(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Bullet-point steps for a creative process
        params = self._get_valid_params()
        decorator = StepByStep(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = StepByStep(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "step_by_step")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = StepByStep.from_dict(serialized)
        self.assertIsInstance(deserialized, StepByStep)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
