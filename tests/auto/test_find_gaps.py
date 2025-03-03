"""Tests for the FindGaps decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.find_gaps import FindGaps

class TestFindGaps(unittest.TestCase):
    """Tests for the FindGaps decorator.

    Identifies missing elements, unanswered questions, or overlooked
    considerations in an idea, plan, or argument. This decorator helps improve
    completeness by systematically discovering and highlighting gaps that need
    addressing.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "aspects": "questions",
            "depth": "basic",
            "solutions": True,
        }

    def test_validate_aspects(self):
        """Test validation for the aspects parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['aspects'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            FindGaps(**params)
        self.assertIn('aspects', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['aspects'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            FindGaps(**params)
        self.assertIn('aspects', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['aspects'] = 'questions'
        # This should not raise an exception
        FindGaps(**params)
        params['aspects'] = 'resources'
        # This should not raise an exception
        FindGaps(**params)
        params['aspects'] = 'stakeholders'
        # This should not raise an exception
        FindGaps(**params)
        params['aspects'] = 'risks'
        # This should not raise an exception
        FindGaps(**params)
        params['aspects'] = 'dependencies'
        # This should not raise an exception
        FindGaps(**params)
        params['aspects'] = 'comprehensive'
        # This should not raise an exception
        FindGaps(**params)

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['depth'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            FindGaps(**params)
        self.assertIn('depth', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['depth'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            FindGaps(**params)
        self.assertIn('depth', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['depth'] = 'basic'
        # This should not raise an exception
        FindGaps(**params)
        params['depth'] = 'thorough'
        # This should not raise an exception
        FindGaps(**params)
        params['depth'] = 'exhaustive'
        # This should not raise an exception
        FindGaps(**params)

    def test_validate_solutions(self):
        """Test validation for the solutions parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['solutions'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            FindGaps(**params)
        self.assertIn('solutions', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic comprehensive gap analysis of a business plan
        params = self._get_valid_params()
        decorator = FindGaps(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Exhaustive stakeholder-focused gap analysis without solutions
        params = self._get_valid_params()
        decorator = FindGaps(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = FindGaps(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "find_gaps")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = FindGaps.from_dict(serialized)
        self.assertIsInstance(deserialized, FindGaps)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)