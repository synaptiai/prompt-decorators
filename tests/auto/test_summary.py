"""Tests for the Summary decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.summary import Summary

class TestSummary(unittest.TestCase):
    """Tests for the Summary decorator.

    Provides a condensed summary of information that would otherwise be
    presented in a more detailed format. This decorator is useful for generating
    executive summaries, article summaries, or concise overviews of complex
    topics.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "length": "short",
            "wordCount": 11,
            "position": "beginning",
        }

    def test_validate_length(self):
        """Test validation for the length parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['length'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('length', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['length'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('length', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['length'] = 'short'
        # This should not raise an exception
        Summary(**params)
        params['length'] = 'medium'
        # This should not raise an exception
        Summary(**params)
        params['length'] = 'long'
        # This should not raise an exception
        Summary(**params)

    def test_validate_wordCount(self):
        """Test validation for the wordCount parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['wordCount'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('wordCount', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['wordCount'] = 9  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('wordCount', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['wordCount'] = 501  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('wordCount', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_position(self):
        """Test validation for the position parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['position'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('position', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['position'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Summary(**params)
        self.assertIn('position', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['position'] = 'beginning'
        # This should not raise an exception
        Summary(**params)
        params['position'] = 'end'
        # This should not raise an exception
        Summary(**params)
        params['position'] = 'standalone'
        # This should not raise an exception
        Summary(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Short standalone summary of a complex topic
        params = self._get_valid_params()
        decorator = Summary(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Specific word count summary at the beginning of a response
        params = self._get_valid_params()
        decorator = Summary(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Summary(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "summary")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Summary.from_dict(serialized)
        self.assertIsInstance(deserialized, Summary)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)