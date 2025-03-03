"""Tests for the Extension decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.extension import Extension


class TestExtension(unittest.TestCase):
    """Tests for the Extension decorator.

    A meta-decorator that enables loading of community-defined decorators from
    external sources. This facilitates the use of specialized decorator
    packages, domain-specific extensions, or custom decorator libraries
    maintained by communities or organizations.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "source": "example_value",
            "version": "example_value",
            "decorators": [],
        }

    def test_missing_required_param_source(self):
        """Test that initialization fails when missing required parameter source."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "source" in params:
            del params["source"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Extension(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "source" in error_message or "required" in error_message.lower()
        )

    def test_validate_source(self):
        """Test validation for the source parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["source"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Extension(**params)
        self.assertIn("source", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_version(self):
        """Test validation for the version parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["version"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Extension(**params)
        self.assertIn("version", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_decorators(self):
        """Test validation for the decorators parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["decorators"] = "not_an_array"  # Not an array
        with self.assertRaises(ValidationError) as context:
            Extension(**params)
        self.assertIn("decorators", str(context.exception))
        self.assertIn("array", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic loading of an extension package
        params = self._get_valid_params()
        decorator = Extension(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Loading specific decorators from a versioned extension
        params = self._get_valid_params()
        decorator = Extension(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Extension(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "extension")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Extension.from_dict(serialized)
        self.assertIsInstance(deserialized, Extension)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
