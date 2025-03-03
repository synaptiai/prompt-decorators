"""Tests for the Creative decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.creative import Creative

class TestCreative(unittest.TestCase):
    """Tests for the Creative decorator.

    Enhances responses with imaginative, novel, and original content. This
    decorator encourages divergent thinking, metaphorical language, and unusual
    connections to generate engaging and non-obvious outputs.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "level": "moderate",
            "elements": [],
            "constraints": [],
        }

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['level'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Creative(**params)
        self.assertIn('level', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['level'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Creative(**params)
        self.assertIn('level', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['level'] = 'moderate'
        # This should not raise an exception
        Creative(**params)
        params['level'] = 'high'
        # This should not raise an exception
        Creative(**params)
        params['level'] = 'unconventional'
        # This should not raise an exception
        Creative(**params)

    def test_validate_elements(self):
        """Test validation for the elements parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['elements'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Creative(**params)
        self.assertIn('elements', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_constraints(self):
        """Test validation for the constraints parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['constraints'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Creative(**params)
        self.assertIn('constraints', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic creative response to a standard question
        params = self._get_valid_params()
        decorator = Creative(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Highly creative response with specific elements
        params = self._get_valid_params()
        decorator = Creative(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Creative(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "creative")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Creative.from_dict(serialized)
        self.assertIsInstance(deserialized, Creative)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)