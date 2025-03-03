"""Tests for the BreakAndBuild decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.break_and_build import BreakAndBuild

class TestBreakAndBuild(unittest.TestCase):
    """Tests for the BreakAndBuild decorator.

    Structures responses in two distinct phases: first critically analyzing and
    'breaking down' an idea by identifying flaws, assumptions, and weaknesses,
    then 'building it back up' with improvements, refinements, and solutions.
    This decorator enhances critical thinking while maintaining constructive
    output.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "breakdown": "weaknesses",
            "intensity": "mild",
            "buildRatio": 1,
        }

    def test_validate_breakdown(self):
        """Test validation for the breakdown parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['breakdown'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('breakdown', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['breakdown'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('breakdown', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['breakdown'] = 'weaknesses'
        # This should not raise an exception
        BreakAndBuild(**params)
        params['breakdown'] = 'assumptions'
        # This should not raise an exception
        BreakAndBuild(**params)
        params['breakdown'] = 'risks'
        # This should not raise an exception
        BreakAndBuild(**params)
        params['breakdown'] = 'comprehensive'
        # This should not raise an exception
        BreakAndBuild(**params)

    def test_validate_intensity(self):
        """Test validation for the intensity parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['intensity'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('intensity', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['intensity'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('intensity', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['intensity'] = 'mild'
        # This should not raise an exception
        BreakAndBuild(**params)
        params['intensity'] = 'thorough'
        # This should not raise an exception
        BreakAndBuild(**params)
        params['intensity'] = 'intense'
        # This should not raise an exception
        BreakAndBuild(**params)

    def test_validate_buildRatio(self):
        """Test validation for the buildRatio parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['buildRatio'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('buildRatio', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['buildRatio'] = -0.5  # Below minimum
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('buildRatio', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['buildRatio'] = 4  # Above maximum
        with self.assertRaises(ValidationError) as context:
            BreakAndBuild(**params)
        self.assertIn('buildRatio', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic break and build analysis of a business concept
        params = self._get_valid_params()
        decorator = BreakAndBuild(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Intense breakdown of assumptions with substantial rebuilding
        params = self._get_valid_params()
        decorator = BreakAndBuild(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = BreakAndBuild(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "break_and_build")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = BreakAndBuild.from_dict(serialized)
        self.assertIsInstance(deserialized, BreakAndBuild)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)