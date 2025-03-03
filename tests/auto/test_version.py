"""Tests for the Version decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.version import Version

class TestVersion(unittest.TestCase):
    """Tests for the Version decorator.

    Specifies the version of the Prompt Decorators standard to use. This
    decorator must be the first in any sequence when used, ensuring proper
    interpretation of decorators according to the specified standard version.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "standard": "1.0.0",
        }


    def test_missing_required_param_standard(self):
        """Test that initialization fails when missing required parameter standard."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "standard" in params:
            del params["standard"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Version(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "standard" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_standard(self):
        """Test validation for the standard parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['standard'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Version(**params)
        self.assertIn('standard', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Specify standard version for compatibility
        params = self._get_valid_params()
        decorator = Version(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Version(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "version")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Version.from_dict(serialized)
        self.assertIsInstance(deserialized, Version)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)