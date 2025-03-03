"""Tests for the Reasoning decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.reasoning import Reasoning

class TestReasoning(unittest.TestCase):
    """Tests for the Reasoning decorator.

    Modifies the AI's response to provide explicit reasoning paths before
    reaching conclusions. This decorator encourages the model to show its
    thought process, making responses more transparent and trustworthy.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "depth": "basic",
        }

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Reasoning(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['depth'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Reasoning(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['depth'] = 'basic'
        # This should not raise an exception
        Reasoning(**params)
        params['depth'] = 'moderate'
        # This should not raise an exception
        Reasoning(**params)
        params['depth'] = 'comprehensive'
        # This should not raise an exception
        Reasoning(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic reasoning for a simple question
        params = self._get_valid_params()
        decorator = Reasoning(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Comprehensive analysis of a complex topic
        params = self._get_valid_params()
        decorator = Reasoning(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Reasoning(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "reasoning")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Reasoning.from_dict(serialized)
        self.assertIsInstance(deserialized, Reasoning)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)