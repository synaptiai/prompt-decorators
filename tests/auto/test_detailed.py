"""Tests for the Detailed decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.detailed import Detailed

class TestDetailed(unittest.TestCase):
    """Tests for the Detailed decorator.

    Enhances the response with comprehensive information, thorough explanations,
    and rich context. This decorator is ideal for in-depth learning, complex
    topics requiring nuance, or when completeness is valued over brevity.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "depth": "moderate",
            "aspects": [],
            "examples": True,
        }

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Detailed(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['depth'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Detailed(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['depth'] = 'moderate'
        # This should not raise an exception
        Detailed(**params)
        params['depth'] = 'comprehensive'
        # This should not raise an exception
        Detailed(**params)
        params['depth'] = 'exhaustive'
        # This should not raise an exception
        Detailed(**params)

    def test_validate_aspects(self):
        """Test validation for the aspects parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['aspects'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Detailed(**params)
        self.assertIn('aspects', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_examples(self):
        """Test validation for the examples parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['examples'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Detailed(**params)
        self.assertIn('examples', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Comprehensive detailed explanation of a concept
        params = self._get_valid_params()
        decorator = Detailed(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Exhaustive detailed analysis of specific aspects
        params = self._get_valid_params()
        decorator = Detailed(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Detailed(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "detailed")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Detailed.from_dict(serialized)
        self.assertIsInstance(deserialized, Detailed)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)