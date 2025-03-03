"""Tests for the Inductive decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.inductive import Inductive

class TestInductive(unittest.TestCase):
    """Tests for the Inductive decorator.

    Structures the response using inductive reasoning, moving from specific
    observations to broader generalizations and theories. This decorator
    emphasizes pattern recognition and the derivation of general principles from
    particular instances.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "examples": 3,
            "confidence": False,
            "structure": "generalization",
        }

    def test_validate_examples(self):
        """Test validation for the examples parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['examples'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('examples', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['examples'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('examples', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['examples'] = 11  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('examples', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_confidence(self):
        """Test validation for the confidence parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['confidence'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('confidence', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_structure(self):
        """Test validation for the structure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['structure'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('structure', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['structure'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Inductive(**params)
        self.assertIn('structure', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['structure'] = 'generalization'
        # This should not raise an exception
        Inductive(**params)
        params['structure'] = 'causal'
        # This should not raise an exception
        Inductive(**params)
        params['structure'] = 'statistical'
        # This should not raise an exception
        Inductive(**params)
        params['structure'] = 'analogical'
        # This should not raise an exception
        Inductive(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic inductive reasoning from examples to general principles
        params = self._get_valid_params()
        decorator = Inductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Causal inductive reasoning with confidence levels
        params = self._get_valid_params()
        decorator = Inductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Inductive(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "inductive")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Inductive.from_dict(serialized)
        self.assertIsInstance(deserialized, Inductive)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)