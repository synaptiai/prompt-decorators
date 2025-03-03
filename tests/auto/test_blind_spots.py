"""Tests for the BlindSpots decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.blind_spots import BlindSpots

class TestBlindSpots(unittest.TestCase):
    """Tests for the BlindSpots decorator.

    Identifies potential cognitive blind spots, unstated assumptions, and
    overlooked perspectives in the response. This decorator helps mitigate bias
    by explicitly acknowledging the limitations of one's thinking and analysis.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "categories": [],
            "depth": "basic",
            "position": "after",
        }

    def test_validate_categories(self):
        """Test validation for the categories parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['categories'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            BlindSpots(**params)
        self.assertIn('categories', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BlindSpots(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['depth'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BlindSpots(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['depth'] = 'basic'
        # This should not raise an exception
        BlindSpots(**params)
        params['depth'] = 'thorough'
        # This should not raise an exception
        BlindSpots(**params)
        params['depth'] = 'comprehensive'
        # This should not raise an exception
        BlindSpots(**params)

    def test_validate_position(self):
        """Test validation for the position parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['position'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BlindSpots(**params)
        self.assertIn('position', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['position'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BlindSpots(**params)
        self.assertIn('position', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['position'] = 'after'
        # This should not raise an exception
        BlindSpots(**params)
        params['position'] = 'before'
        # This should not raise an exception
        BlindSpots(**params)
        params['position'] = 'integrated'
        # This should not raise an exception
        BlindSpots(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic blind spots analysis after a response
        params = self._get_valid_params()
        decorator = BlindSpots(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Comprehensive blind spots analysis integrated throughout
        params = self._get_valid_params()
        decorator = BlindSpots(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = BlindSpots(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "blind_spots")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = BlindSpots.from_dict(serialized)
        self.assertIsInstance(deserialized, BlindSpots)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)