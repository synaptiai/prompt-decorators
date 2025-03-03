"""Tests for the RedTeam decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.red_team import RedTeam

class TestRedTeam(unittest.TestCase):
    """Tests for the RedTeam decorator.

    Applies adversarial analysis to test assumptions, identify vulnerabilities,
    and strengthen proposals by actively looking for flaws. This decorator
    simulates how an opponent or critic would evaluate and attack ideas, plans,
    or arguments.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "strength": "moderate",
            "focus": [],
            "constructive": True,
        }

    def test_validate_strength(self):
        """Test validation for the strength parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['strength'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            RedTeam(**params)
        self.assertIn('strength', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['strength'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            RedTeam(**params)
        self.assertIn('strength', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['strength'] = 'moderate'
        # This should not raise an exception
        RedTeam(**params)
        params['strength'] = 'aggressive'
        # This should not raise an exception
        RedTeam(**params)
        params['strength'] = 'steelman'
        # This should not raise an exception
        RedTeam(**params)

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['focus'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            RedTeam(**params)
        self.assertIn('focus', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_constructive(self):
        """Test validation for the constructive parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['constructive'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            RedTeam(**params)
        self.assertIn('constructive', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic red team analysis of a business proposal
        params = self._get_valid_params()
        decorator = RedTeam(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Aggressive red team analysis with specific focus areas
        params = self._get_valid_params()
        decorator = RedTeam(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = RedTeam(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "red_team")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = RedTeam.from_dict(serialized)
        self.assertIsInstance(deserialized, RedTeam)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)