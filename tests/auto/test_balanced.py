"""Tests for the Balanced decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.balanced import Balanced

class TestBalanced(unittest.TestCase):
    """Tests for the Balanced decorator.

    Ensures equal representation of different perspectives or viewpoints on a
    topic. This decorator promotes fairness and comprehensiveness by giving
    proportional attention to multiple sides of an issue, avoiding bias toward
    any particular position.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "perspectives": 2,
            "structure": "alternating",
            "equal": True,
        }

    def test_validate_perspectives(self):
        """Test validation for the perspectives parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['perspectives'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('perspectives', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['perspectives'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('perspectives', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['perspectives'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('perspectives', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_structure(self):
        """Test validation for the structure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['structure'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('structure', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['structure'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('structure', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['structure'] = 'alternating'
        # This should not raise an exception
        Balanced(**params)
        params['structure'] = 'sequential'
        # This should not raise an exception
        Balanced(**params)
        params['structure'] = 'comparative'
        # This should not raise an exception
        Balanced(**params)

    def test_validate_equal(self):
        """Test validation for the equal parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['equal'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Balanced(**params)
        self.assertIn('equal', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic balanced view of a controversial topic
        params = self._get_valid_params()
        decorator = Balanced(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Balanced presentation of multiple perspectives in comparative structure
        params = self._get_valid_params()
        decorator = Balanced(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Balanced(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "balanced")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Balanced.from_dict(serialized)
        self.assertIsInstance(deserialized, Balanced)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)