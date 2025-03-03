"""Tests for the Socratic decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.socratic import Socratic

class TestSocratic(unittest.TestCase):
    """Tests for the Socratic decorator.

    Structures the response as a series of questions that guide the user through
    a problem or topic. This decorator encourages critical thinking through
    question-based exploration, helping to uncover assumptions and lead to
    deeper understanding.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "iterations": 3,
        }

    def test_validate_iterations(self):
        """Test validation for the iterations parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['iterations'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Socratic(**params)
        self.assertIn('iterations', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['iterations'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Socratic(**params)
        self.assertIn('iterations', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['iterations'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Socratic(**params)
        self.assertIn('iterations', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic socratic exploration of a philosophical concept
        params = self._get_valid_params()
        decorator = Socratic(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Deep socratic analysis with 5 iterations
        params = self._get_valid_params()
        decorator = Socratic(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Socratic(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "socratic")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Socratic.from_dict(serialized)
        self.assertIsInstance(deserialized, Socratic)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)