"""Tests for the Timeline decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.timeline import Timeline

class TestTimeline(unittest.TestCase):
    """Tests for the Timeline decorator.

    Organizes information in chronological order, highlighting key events or
    developments over time. This decorator is ideal for historical accounts,
    project planning, process evolution, or any topic with a temporal dimension.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "granularity": "day",
            "format": "list",
            "details": "minimal",
        }

    def test_validate_granularity(self):
        """Test validation for the granularity parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['granularity'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('granularity', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['granularity'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('granularity', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['granularity'] = 'day'
        # This should not raise an exception
        Timeline(**params)
        params['granularity'] = 'month'
        # This should not raise an exception
        Timeline(**params)
        params['granularity'] = 'year'
        # This should not raise an exception
        Timeline(**params)
        params['granularity'] = 'decade'
        # This should not raise an exception
        Timeline(**params)
        params['granularity'] = 'century'
        # This should not raise an exception
        Timeline(**params)
        params['granularity'] = 'era'
        # This should not raise an exception
        Timeline(**params)

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['format'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('format', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['format'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('format', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['format'] = 'list'
        # This should not raise an exception
        Timeline(**params)
        params['format'] = 'narrative'
        # This should not raise an exception
        Timeline(**params)
        params['format'] = 'table'
        # This should not raise an exception
        Timeline(**params)

    def test_validate_details(self):
        """Test validation for the details parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['details'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('details', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['details'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Timeline(**params)
        self.assertIn('details', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['details'] = 'minimal'
        # This should not raise an exception
        Timeline(**params)
        params['details'] = 'moderate'
        # This should not raise an exception
        Timeline(**params)
        params['details'] = 'comprehensive'
        # This should not raise an exception
        Timeline(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic chronological timeline of major events
        params = self._get_valid_params()
        decorator = Timeline(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed narrative timeline with specific date granularity
        params = self._get_valid_params()
        decorator = Timeline(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Timeline(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "timeline")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Timeline.from_dict(serialized)
        self.assertIsInstance(deserialized, Timeline)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)