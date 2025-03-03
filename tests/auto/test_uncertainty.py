"""Tests for the Uncertainty decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.uncertainty import Uncertainty

class TestUncertainty(unittest.TestCase):
    """Tests for the Uncertainty decorator.

    Explicitly highlights areas of uncertainty in the response. This decorator
    promotes intellectual honesty by clearly indicating what is known with
    confidence versus what is speculative, unknown, or subject to debate.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "format": "inline",
            "threshold": "low",
            "reason": False,
        }

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['format'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Uncertainty(**params)
        self.assertIn('format', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['format'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Uncertainty(**params)
        self.assertIn('format', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['format'] = 'inline'
        # This should not raise an exception
        Uncertainty(**params)
        params['format'] = 'section'
        # This should not raise an exception
        Uncertainty(**params)
        params['format'] = 'confidence'
        # This should not raise an exception
        Uncertainty(**params)

    def test_validate_threshold(self):
        """Test validation for the threshold parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['threshold'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Uncertainty(**params)
        self.assertIn('threshold', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['threshold'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Uncertainty(**params)
        self.assertIn('threshold', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['threshold'] = 'low'
        # This should not raise an exception
        Uncertainty(**params)
        params['threshold'] = 'medium'
        # This should not raise an exception
        Uncertainty(**params)
        params['threshold'] = 'high'
        # This should not raise an exception
        Uncertainty(**params)

    def test_validate_reason(self):
        """Test validation for the reason parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['reason'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Uncertainty(**params)
        self.assertIn('reason', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Inline uncertainty markers in a technical explanation
        params = self._get_valid_params()
        decorator = Uncertainty(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Dedicated uncertainty section with detailed reasoning
        params = self._get_valid_params()
        decorator = Uncertainty(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Uncertainty(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "uncertainty")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Uncertainty.from_dict(serialized)
        self.assertIsInstance(deserialized, Uncertainty)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)