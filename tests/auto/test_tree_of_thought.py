"""Tests for the TreeOfThought decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.tree_of_thought import TreeOfThought

class TestTreeOfThought(unittest.TestCase):
    """Tests for the TreeOfThought decorator.

    Organizes the response as a branching exploration of multiple reasoning
    paths. This decorator enables the AI to consider several possible approaches
    or hypotheses simultaneously, exploring the implications of each before
    reaching conclusions.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "branches": 3,
            "depth": 3,
            "pruning": False,
        }

    def test_validate_branches(self):
        """Test validation for the branches parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['branches'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('branches', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['branches'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('branches', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['branches'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('branches', str(context.exception))
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
            TreeOfThought(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['depth'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['depth'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_pruning(self):
        """Test validation for the pruning parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['pruning'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            TreeOfThought(**params)
        self.assertIn('pruning', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Multi-branch problem solving for a complex question
        params = self._get_valid_params()
        decorator = TreeOfThought(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Deep, focused exploration with pruning
        params = self._get_valid_params()
        decorator = TreeOfThought(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = TreeOfThought(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "tree_of_thought")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = TreeOfThought.from_dict(serialized)
        self.assertIsInstance(deserialized, TreeOfThought)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)