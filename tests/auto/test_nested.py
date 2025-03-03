"""Tests for the Nested decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.nested import Nested

class TestNested(unittest.TestCase):
    """Tests for the Nested decorator.

    Organizes information in a deeply hierarchical structure with multiple
    levels of nesting. This decorator is ideal for complex topics with many
    subcategories, helping to maintain clarity through consistent organization
    patterns.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "depth": 3,
            "style": "bullet",
            "collapsible": False,
        }

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['depth'] = 1  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['depth'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['style'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('style', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['style'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('style', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['style'] = 'bullet'
        # This should not raise an exception
        Nested(**params)
        params['style'] = 'numbered'
        # This should not raise an exception
        Nested(**params)
        params['style'] = 'mixed'
        # This should not raise an exception
        Nested(**params)

    def test_validate_collapsible(self):
        """Test validation for the collapsible parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['collapsible'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Nested(**params)
        self.assertIn('collapsible', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Deep hierarchical organization of a complex domain
        params = self._get_valid_params()
        decorator = Nested(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Maximum depth collapsible structure for reference material
        params = self._get_valid_params()
        decorator = Nested(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Nested(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "nested")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Nested.from_dict(serialized)
        self.assertIsInstance(deserialized, Nested)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)