"""Tests for the Deductive decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.deductive import Deductive

class TestDeductive(unittest.TestCase):
    """Tests for the Deductive decorator.

    Structures the response using deductive reasoning, moving from general
    principles to specific conclusions. This decorator emphasizes logical
    argument development, starting with premises and working methodically to
    necessary conclusions.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "premises": 2,
            "formal": False,
            "steps": 3,
        }

    def test_validate_premises(self):
        """Test validation for the premises parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['premises'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('premises', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['premises'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('premises', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['premises'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('premises', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_formal(self):
        """Test validation for the formal parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['formal'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('formal', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_steps(self):
        """Test validation for the steps parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['steps'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('steps', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['steps'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('steps', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['steps'] = 8  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Deductive(**params)
        self.assertIn('steps', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic deductive reasoning from principles to specific conclusions
        params = self._get_valid_params()
        decorator = Deductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Formal deductive logic with multiple steps
        params = self._get_valid_params()
        decorator = Deductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Deductive(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "deductive")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Deductive.from_dict(serialized)
        self.assertIsInstance(deserialized, Deductive)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)