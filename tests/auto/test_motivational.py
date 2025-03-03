"""Tests for the Motivational decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.motivational import Motivational

class TestMotivational(unittest.TestCase):
    """Tests for the Motivational decorator.

    Enhances responses with encouraging, inspiring, and empowering language.
    This decorator is designed to motivate action, build confidence, and create
    a positive emotional impact while still delivering substantive content.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "intensity": "mild",
            "focus": "achievement",
            "actionable": True,
        }

    def test_validate_intensity(self):
        """Test validation for the intensity parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['intensity'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Motivational(**params)
        self.assertIn('intensity', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['intensity'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Motivational(**params)
        self.assertIn('intensity', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['intensity'] = 'mild'
        # This should not raise an exception
        Motivational(**params)
        params['intensity'] = 'moderate'
        # This should not raise an exception
        Motivational(**params)
        params['intensity'] = 'high'
        # This should not raise an exception
        Motivational(**params)

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['focus'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Motivational(**params)
        self.assertIn('focus', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['focus'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Motivational(**params)
        self.assertIn('focus', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['focus'] = 'achievement'
        # This should not raise an exception
        Motivational(**params)
        params['focus'] = 'growth'
        # This should not raise an exception
        Motivational(**params)
        params['focus'] = 'resilience'
        # This should not raise an exception
        Motivational(**params)
        params['focus'] = 'purpose'
        # This should not raise an exception
        Motivational(**params)
        params['focus'] = 'balanced'
        # This should not raise an exception
        Motivational(**params)

    def test_validate_actionable(self):
        """Test validation for the actionable parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['actionable'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Motivational(**params)
        self.assertIn('actionable', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic moderately motivational response
        params = self._get_valid_params()
        decorator = Motivational(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # High-intensity resilience-focused motivational content
        params = self._get_valid_params()
        decorator = Motivational(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Motivational(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "motivational")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Motivational.from_dict(serialized)
        self.assertIsInstance(deserialized, Motivational)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)