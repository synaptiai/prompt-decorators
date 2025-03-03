"""Tests for the Compatibility decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.compatibility import Compatibility

class TestCompatibility(unittest.TestCase):
    """Tests for the Compatibility decorator.

    A meta-decorator that specifies model-specific adaptations or fall-back
    behaviors. This enables graceful degradation of decorator functionalities
    across different LLM capabilities and ensures optimal performance across
    model variants.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "models": [],
            "fallback": "example_value",
            "behaviors": "example_value",
        }


    def test_missing_required_param_models(self):
        """Test that initialization fails when missing required parameter models."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "models" in params:
            del params["models"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Compatibility(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "models" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_models(self):
        """Test validation for the models parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['models'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Compatibility(**params)
        self.assertIn('models', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_fallback(self):
        """Test validation for the fallback parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['fallback'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Compatibility(**params)
        self.assertIn('fallback', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_behaviors(self):
        """Test validation for the behaviors parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['behaviors'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Compatibility(**params)
        self.assertIn('behaviors', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic model-specific adaptation
        params = self._get_valid_params()
        decorator = Compatibility(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed model-specific behavior adaptations
        params = self._get_valid_params()
        decorator = Compatibility(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Compatibility(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "compatibility")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Compatibility.from_dict(serialized)
        self.assertIsInstance(deserialized, Compatibility)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)