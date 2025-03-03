"""Tests for the Chain decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.chain import Chain

class TestChain(unittest.TestCase):
    """Tests for the Chain decorator.

    A meta-decorator that applies multiple decorators in sequence, with each
    decorator processing the output of the previous one. This enables complex
    transformations by combining multiple simpler decorators in a pipeline.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "decorators": [],
            "showSteps": False,
            "stopOnFailure": True,
        }


    def test_missing_required_param_decorators(self):
        """Test that initialization fails when missing required parameter decorators."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "decorators" in params:
            del params["decorators"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Chain(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "decorators" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_decorators(self):
        """Test validation for the decorators parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['decorators'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Chain(**params)
        self.assertIn('decorators', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_showSteps(self):
        """Test validation for the showSteps parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['showSteps'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Chain(**params)
        self.assertIn('showSteps', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_stopOnFailure(self):
        """Test validation for the stopOnFailure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['stopOnFailure'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Chain(**params)
        self.assertIn('stopOnFailure', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic sequential application of decorators
        params = self._get_valid_params()
        decorator = Chain(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Complex decorator chain with visible intermediate steps
        params = self._get_valid_params()
        decorator = Chain(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Chain(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "chain")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Chain.from_dict(serialized)
        self.assertIsInstance(deserialized, Chain)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)