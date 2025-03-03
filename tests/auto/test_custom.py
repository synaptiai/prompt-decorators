"""Tests for the Custom decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.custom import Custom

class TestCustom(unittest.TestCase):
    """Tests for the Custom decorator.

    A meta-decorator that enables user-defined decorator behaviors through
    explicit rules or instructions. This provides maximum flexibility for
    creating specialized behaviors not covered by standard decorators.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "rules": "example_value",
            "name": "example_value",
            "priority": "override",
        }


    def test_missing_required_param_rules(self):
        """Test that initialization fails when missing required parameter rules."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "rules" in params:
            del params["rules"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Custom(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "rules" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_rules(self):
        """Test validation for the rules parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['rules'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Custom(**params)
        self.assertIn('rules', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_name(self):
        """Test validation for the name parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['name'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Custom(**params)
        self.assertIn('name', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_priority(self):
        """Test validation for the priority parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['priority'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Custom(**params)
        self.assertIn('priority', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['priority'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Custom(**params)
        self.assertIn('priority', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['priority'] = 'override'
        # This should not raise an exception
        Custom(**params)
        params['priority'] = 'supplement'
        # This should not raise an exception
        Custom(**params)
        params['priority'] = 'fallback'
        # This should not raise an exception
        Custom(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic custom formatting rule
        params = self._get_valid_params()
        decorator = Custom(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Complex custom behavior with named reference
        params = self._get_valid_params()
        decorator = Custom(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Custom(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "custom")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Custom.from_dict(serialized)
        self.assertIsInstance(deserialized, Custom)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)