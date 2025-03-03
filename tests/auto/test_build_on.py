"""Tests for the BuildOn decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.build_on import BuildOn

class TestBuildOn(unittest.TestCase):
    """Tests for the BuildOn decorator.

    A meta-decorator that builds upon previous context or responses rather than
    starting from scratch. This enables continuity across interactions, allowing
    refinement, extension, or alteration of previous outputs in a coherent
    manner.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "reference": "last",
            "approach": "extend",
            "preserveStructure": True,
        }

    def test_validate_reference(self):
        """Test validation for the reference parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['reference'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BuildOn(**params)
        self.assertIn('reference', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['reference'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BuildOn(**params)
        self.assertIn('reference', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['reference'] = 'last'
        # This should not raise an exception
        BuildOn(**params)
        params['reference'] = 'specific'
        # This should not raise an exception
        BuildOn(**params)
        params['reference'] = 'all'
        # This should not raise an exception
        BuildOn(**params)

    def test_validate_approach(self):
        """Test validation for the approach parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['approach'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BuildOn(**params)
        self.assertIn('approach', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['approach'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BuildOn(**params)
        self.assertIn('approach', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['approach'] = 'extend'
        # This should not raise an exception
        BuildOn(**params)
        params['approach'] = 'refine'
        # This should not raise an exception
        BuildOn(**params)
        params['approach'] = 'contrast'
        # This should not raise an exception
        BuildOn(**params)
        params['approach'] = 'synthesize'
        # This should not raise an exception
        BuildOn(**params)

    def test_validate_preserveStructure(self):
        """Test validation for the preserveStructure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['preserveStructure'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            BuildOn(**params)
        self.assertIn('preserveStructure', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic extension of the previous response
        params = self._get_valid_params()
        decorator = BuildOn(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Specific refinement with structural changes
        params = self._get_valid_params()
        decorator = BuildOn(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = BuildOn(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "build_on")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = BuildOn.from_dict(serialized)
        self.assertIsInstance(deserialized, BuildOn)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)