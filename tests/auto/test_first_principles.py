"""Tests for the FirstPrinciples decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.first_principles import FirstPrinciples

class TestFirstPrinciples(unittest.TestCase):
    """Tests for the FirstPrinciples decorator.

    Structures the response by breaking down complex topics into their
    fundamental truths or axioms, then building up from there. This decorator
    promotes a deeper understanding by examining the most basic elements of a
    concept before constructing more complex ideas.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "depth": 3,
        }

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            FirstPrinciples(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['depth'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            FirstPrinciples(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['depth'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            FirstPrinciples(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic first principles analysis of a concept
        params = self._get_valid_params()
        decorator = FirstPrinciples(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Deep first principles analysis with maximum depth
        params = self._get_valid_params()
        decorator = FirstPrinciples(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = FirstPrinciples(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "first_principles")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = FirstPrinciples.from_dict(serialized)
        self.assertIsInstance(deserialized, FirstPrinciples)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)