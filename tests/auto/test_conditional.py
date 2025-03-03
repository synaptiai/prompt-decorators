"""Tests for the Conditional decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.conditional import Conditional


class TestConditional(unittest.TestCase):
    """Tests for the Conditional decorator.

    A meta-decorator that applies different decorators based on specified
    conditions. This enables dynamic behavior where the response formatting and
    approach changes depending on the content, context, or user-specified
    parameters.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "if_param": "example_value",
            "then": "example_value",
            "else_param": "example_value",
        }

    def test_missing_required_param_if_param(self):
        """Test that initialization fails when missing required parameter if_param."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "if_param" in params:
            del params["if_param"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Conditional(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "if_param" in error_message or "required" in error_message.lower()
        )

    def test_missing_required_param_then(self):
        """Test that initialization fails when missing required parameter then."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "then" in params:
            del params["then"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Conditional(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue("then" in error_message or "required" in error_message.lower())

    def test_validate_if_param(self):
        """Test validation for the if_param parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["if_param"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Conditional(**params)
        self.assertIn("if_param", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_then(self):
        """Test validation for the then parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["then"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Conditional(**params)
        self.assertIn("then", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_else_param(self):
        """Test validation for the else_param parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["else_param"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Conditional(**params)
        self.assertIn("else_param", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic conditional application based on content complexity
        params = self._get_valid_params()
        decorator = Conditional(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Conditional application with parameterized decorators
        params = self._get_valid_params()
        decorator = Conditional(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Conditional(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "conditional")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Conditional.from_dict(serialized)
        self.assertIsInstance(deserialized, Conditional)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
