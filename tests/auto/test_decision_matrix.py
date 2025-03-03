"""Tests for the DecisionMatrix decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.decision_matrix import DecisionMatrix

class TestDecisionMatrix(unittest.TestCase):
    """Tests for the DecisionMatrix decorator.

    Structures the response as a decision matrix, evaluating options against
    multiple criteria. This decorator facilitates systematic comparison and
    selection between alternatives based on weighted or unweighted criteria.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "options": [],
            "criteria": [],
            "weighted": False,
            "scale": "1-5",
        }

    def test_validate_options(self):
        """Test validation for the options parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['options'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            DecisionMatrix(**params)
        self.assertIn('options', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_criteria(self):
        """Test validation for the criteria parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['criteria'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            DecisionMatrix(**params)
        self.assertIn('criteria', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_weighted(self):
        """Test validation for the weighted parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['weighted'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            DecisionMatrix(**params)
        self.assertIn('weighted', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_scale(self):
        """Test validation for the scale parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['scale'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            DecisionMatrix(**params)
        self.assertIn('scale', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['scale'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            DecisionMatrix(**params)
        self.assertIn('scale', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['scale'] = '1-5'
        # This should not raise an exception
        DecisionMatrix(**params)
        params['scale'] = '1-10'
        # This should not raise an exception
        DecisionMatrix(**params)
        params['scale'] = 'qualitative'
        # This should not raise an exception
        DecisionMatrix(**params)
        params['scale'] = 'percentage'
        # This should not raise an exception
        DecisionMatrix(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Simple decision matrix for comparing options
        params = self._get_valid_params()
        decorator = DecisionMatrix(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Weighted decision matrix with custom options and criteria
        params = self._get_valid_params()
        decorator = DecisionMatrix(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = DecisionMatrix(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "decision_matrix")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = DecisionMatrix.from_dict(serialized)
        self.assertIsInstance(deserialized, DecisionMatrix)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)