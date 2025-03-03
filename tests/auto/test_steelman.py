"""Tests for the Steelman decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.steelman import Steelman

class TestSteelman(unittest.TestCase):
    """Tests for the Steelman decorator.

    Presents the strongest possible version of an argument or position, even
    those the AI might not agree with. This decorator opposes strawman fallacies
    by ensuring each viewpoint is represented in its most compelling and
    charitable form.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "sides": 2,
            "critique": False,
            "separation": True,
        }

    def test_validate_sides(self):
        """Test validation for the sides parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['sides'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Steelman(**params)
        self.assertIn('sides', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['sides'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Steelman(**params)
        self.assertIn('sides', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['sides'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Steelman(**params)
        self.assertIn('sides', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_critique(self):
        """Test validation for the critique parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['critique'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Steelman(**params)
        self.assertIn('critique', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_separation(self):
        """Test validation for the separation parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['separation'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Steelman(**params)
        self.assertIn('separation', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Steel-manning both sides of a controversial issue
        params = self._get_valid_params()
        decorator = Steelman(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Steel-manning one position with subsequent critique
        params = self._get_valid_params()
        decorator = Steelman(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Steelman(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "steelman")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Steelman.from_dict(serialized)
        self.assertIsInstance(deserialized, Steelman)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)