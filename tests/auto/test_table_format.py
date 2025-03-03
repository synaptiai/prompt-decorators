"""Tests for the TableFormat decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.table_format import TableFormat

class TestTableFormat(unittest.TestCase):
    """Tests for the TableFormat decorator.

    Structures the AI's response in a tabular format with defined columns. This
    decorator is ideal for presenting comparative data, lists of items with
    attributes, or any information that benefits from clear columnar
    organization.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "columns": [],
            "format": "markdown",
            "alignment": "left",
        }


    def test_missing_required_param_columns(self):
        """Test that initialization fails when missing required parameter columns."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "columns" in params:
            del params["columns"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            TableFormat(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "columns" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_columns(self):
        """Test validation for the columns parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['columns'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            TableFormat(**params)
        self.assertIn('columns', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['format'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            TableFormat(**params)
        self.assertIn('format', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['format'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            TableFormat(**params)
        self.assertIn('format', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['format'] = 'markdown'
        # This should not raise an exception
        TableFormat(**params)
        params['format'] = 'ascii'
        # This should not raise an exception
        TableFormat(**params)
        params['format'] = 'csv'
        # This should not raise an exception
        TableFormat(**params)

    def test_validate_alignment(self):
        """Test validation for the alignment parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['alignment'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            TableFormat(**params)
        self.assertIn('alignment', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['alignment'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            TableFormat(**params)
        self.assertIn('alignment', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['alignment'] = 'left'
        # This should not raise an exception
        TableFormat(**params)
        params['alignment'] = 'center'
        # This should not raise an exception
        TableFormat(**params)
        params['alignment'] = 'right'
        # This should not raise an exception
        TableFormat(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Simple comparison table in markdown format
        params = self._get_valid_params()
        decorator = TableFormat(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed CSV table with specific columns
        params = self._get_valid_params()
        decorator = TableFormat(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = TableFormat(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "table_format")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = TableFormat.from_dict(serialized)
        self.assertIsInstance(deserialized, TableFormat)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)