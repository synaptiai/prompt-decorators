"""Tests for the Remix decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.remix import Remix

class TestRemix(unittest.TestCase):
    """Tests for the Remix decorator.

    Reframes or adapts content for a different context, purpose, or audience
    than originally intended. This decorator transforms the presentation style
    while preserving core information, making it accessible and relevant to
    specific scenarios or demographics.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "target": "example_value",
            "preserve": "facts",
            "contrast": False,
        }


    def test_missing_required_param_target(self):
        """Test that initialization fails when missing required parameter target."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "target" in params:
            del params["target"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Remix(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "target" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_target(self):
        """Test validation for the target parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['target'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Remix(**params)
        self.assertIn('target', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_preserve(self):
        """Test validation for the preserve parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['preserve'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Remix(**params)
        self.assertIn('preserve', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['preserve'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Remix(**params)
        self.assertIn('preserve', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['preserve'] = 'facts'
        # This should not raise an exception
        Remix(**params)
        params['preserve'] = 'structure'
        # This should not raise an exception
        Remix(**params)
        params['preserve'] = 'tone'
        # This should not raise an exception
        Remix(**params)
        params['preserve'] = 'comprehensiveness'
        # This should not raise an exception
        Remix(**params)

    def test_validate_contrast(self):
        """Test validation for the contrast parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['contrast'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Remix(**params)
        self.assertIn('contrast', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic remix for a different audience
        params = self._get_valid_params()
        decorator = Remix(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Business remix with contrasting approach
        params = self._get_valid_params()
        decorator = Remix(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Remix(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "remix")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Remix.from_dict(serialized)
        self.assertIsInstance(deserialized, Remix)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)