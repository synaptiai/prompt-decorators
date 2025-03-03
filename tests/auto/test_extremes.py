"""Tests for the Extremes decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.extremes import Extremes

class TestExtremes(unittest.TestCase):
    """Tests for the Extremes decorator.

    Presents content at the extreme ends of a spectrum, showing both a radical,
    ambitious, or maximalist version alongside a minimal, conservative, or basic
    version. This decorator helps explore the range of possibilities from the
    simplest implementation to the most expansive vision.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "versions": "radical",
            "dimension": "ambition",
            "compare": True,
        }

    def test_validate_versions(self):
        """Test validation for the versions parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['versions'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Extremes(**params)
        self.assertIn('versions', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['versions'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Extremes(**params)
        self.assertIn('versions', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['versions'] = 'radical'
        # This should not raise an exception
        Extremes(**params)
        params['versions'] = 'minimal'
        # This should not raise an exception
        Extremes(**params)
        params['versions'] = 'both'
        # This should not raise an exception
        Extremes(**params)

    def test_validate_dimension(self):
        """Test validation for the dimension parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['dimension'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Extremes(**params)
        self.assertIn('dimension', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_compare(self):
        """Test validation for the compare parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['compare'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Extremes(**params)
        self.assertIn('compare', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic exploration of minimal and radical approaches
        params = self._get_valid_params()
        decorator = Extremes(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Only radical version along a specific dimension
        params = self._get_valid_params()
        decorator = Extremes(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Extremes(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "extremes")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Extremes.from_dict(serialized)
        self.assertIsInstance(deserialized, Extremes)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)