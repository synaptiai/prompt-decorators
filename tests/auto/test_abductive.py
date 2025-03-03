"""Tests for the Abductive decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.abductive import Abductive

class TestAbductive(unittest.TestCase):
    """Tests for the Abductive decorator.

    Structures the response using abductive reasoning, developing the most
    likely explanations for observations or phenomena. This decorator emphasizes
    inference to the best explanation and hypothetical reasoning to address
    incomplete information.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "hypotheses": 3,
            "criteria": [],
            "rank": True,
        }

    def test_validate_hypotheses(self):
        """Test validation for the hypotheses parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['hypotheses'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Abductive(**params)
        self.assertIn('hypotheses', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['hypotheses'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Abductive(**params)
        self.assertIn('hypotheses', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['hypotheses'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Abductive(**params)
        self.assertIn('hypotheses', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_criteria(self):
        """Test validation for the criteria parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['criteria'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Abductive(**params)
        self.assertIn('criteria', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_rank(self):
        """Test validation for the rank parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['rank'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Abductive(**params)
        self.assertIn('rank', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic abductive reasoning with multiple hypotheses
        params = self._get_valid_params()
        decorator = Abductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed abductive reasoning with specific evaluation criteria
        params = self._get_valid_params()
        decorator = Abductive(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Abductive(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "abductive")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Abductive.from_dict(serialized)
        self.assertIsInstance(deserialized, Abductive)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)