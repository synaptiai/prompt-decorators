"""Tests for the Schema decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.schema import Schema

class TestSchema(unittest.TestCase):
    """Tests for the Schema decorator.

    Defines a custom structure for the AI's response using a specified schema
    format. This decorator enables precise control over the output structure,
    ensuring responses follow a consistent, well-defined format optimized for
    specific use cases or data processing needs.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "schema": "example_value",
            "strict": False,
        }


    def test_missing_required_param_schema(self):
        """Test that initialization fails when missing required parameter schema."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "schema" in params:
            del params["schema"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Schema(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "schema" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_schema(self):
        """Test validation for the schema parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['schema'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Schema(**params)
        self.assertIn('schema', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_strict(self):
        """Test validation for the strict parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['strict'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Schema(**params)
        self.assertIn('strict', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic schema for a person's information
        params = self._get_valid_params()
        decorator = Schema(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Strict schema for product information
        params = self._get_valid_params()
        decorator = Schema(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Schema(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "schema")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Schema.from_dict(serialized)
        self.assertIsInstance(deserialized, Schema)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)