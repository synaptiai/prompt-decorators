"""Tests for the Limitations decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.limitations import Limitations

class TestLimitations(unittest.TestCase):
    """Tests for the Limitations decorator.

    Adds an explicit statement of limitations, caveats, or uncertainties related
    to the provided information. This decorator promotes intellectual honesty by
    acknowledging the boundaries of current knowledge, potential biases, or
    contextual constraints.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "detail": "brief",
            "position": "beginning",
            "focus": "knowledge",
        }

    def test_validate_detail(self):
        """Test validation for the detail parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['detail'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('detail', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['detail'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('detail', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['detail'] = 'brief'
        # This should not raise an exception
        Limitations(**params)
        params['detail'] = 'moderate'
        # This should not raise an exception
        Limitations(**params)
        params['detail'] = 'comprehensive'
        # This should not raise an exception
        Limitations(**params)

    def test_validate_position(self):
        """Test validation for the position parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['position'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('position', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['position'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('position', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['position'] = 'beginning'
        # This should not raise an exception
        Limitations(**params)
        params['position'] = 'end'
        # This should not raise an exception
        Limitations(**params)

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['focus'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('focus', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['focus'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Limitations(**params)
        self.assertIn('focus', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['focus'] = 'knowledge'
        # This should not raise an exception
        Limitations(**params)
        params['focus'] = 'methodology'
        # This should not raise an exception
        Limitations(**params)
        params['focus'] = 'context'
        # This should not raise an exception
        Limitations(**params)
        params['focus'] = 'biases'
        # This should not raise an exception
        Limitations(**params)
        params['focus'] = 'all'
        # This should not raise an exception
        Limitations(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Brief limitations statement at the end focused on methodology
        params = self._get_valid_params()
        decorator = Limitations(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Comprehensive limitations at the beginning covering all aspects
        params = self._get_valid_params()
        decorator = Limitations(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Limitations(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "limitations")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Limitations.from_dict(serialized)
        self.assertIsInstance(deserialized, Limitations)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)