"""Tests for the MECE decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.mece import MECE

class TestMECE(unittest.TestCase):
    """Tests for the MECE decorator.

    Structures the response using the Mutually Exclusive, Collectively
    Exhaustive framework - a principle where categories have no overlaps and
    cover all possibilities. This decorator ensures comprehensive analysis with
    clear categorization for decision-making and problem-solving.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "dimensions": 3,
            "depth": 2,
            "framework": "issue tree",
        }

    def test_validate_dimensions(self):
        """Test validation for the dimensions parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['dimensions'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('dimensions', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['dimensions'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('dimensions', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['dimensions'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('dimensions', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['depth'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['depth'] = 4  # Above maximum
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_framework(self):
        """Test validation for the framework parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['framework'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('framework', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['framework'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            MECE(**params)
        self.assertIn('framework', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['framework'] = 'issue tree'
        # This should not raise an exception
        MECE(**params)
        params['framework'] = 'value chain'
        # This should not raise an exception
        MECE(**params)
        params['framework'] = 'business segments'
        # This should not raise an exception
        MECE(**params)
        params['framework'] = 'stakeholders'
        # This should not raise an exception
        MECE(**params)
        params['framework'] = 'custom'
        # This should not raise an exception
        MECE(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic MECE analysis of a business problem
        params = self._get_valid_params()
        decorator = MECE(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed MECE framework with stakeholder focus
        params = self._get_valid_params()
        decorator = MECE(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = MECE(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "mece")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = MECE.from_dict(serialized)
        self.assertIsInstance(deserialized, MECE)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)