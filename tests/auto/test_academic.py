"""Tests for the Academic decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.academic import Academic


class TestAcademic(unittest.TestCase):
    """Tests for the Academic decorator.

    Adapts the response to follow scholarly writing conventions appropriate for
    academic publications. This decorator generates responses with formal
    language, structured argumentation, and proper citations following
    established academic citation styles.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "style": "humanities",
            "format": "APA",
        }

    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["style"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Academic(**params)
        self.assertIn("style", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["style"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Academic(**params)
        self.assertIn("style", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["style"] = "humanities"
        # This should not raise an exception
        Academic(**params)
        params["style"] = "scientific"
        # This should not raise an exception
        Academic(**params)
        params["style"] = "legal"
        # This should not raise an exception
        Academic(**params)

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["format"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Academic(**params)
        self.assertIn("format", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["format"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Academic(**params)
        self.assertIn("format", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["format"] = "APA"
        # This should not raise an exception
        Academic(**params)
        params["format"] = "MLA"
        # This should not raise an exception
        Academic(**params)
        params["format"] = "Chicago"
        # This should not raise an exception
        Academic(**params)
        params["format"] = "Harvard"
        # This should not raise an exception
        Academic(**params)
        params["format"] = "IEEE"
        # This should not raise an exception
        Academic(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Scientific academic response with APA citations
        params = self._get_valid_params()
        decorator = Academic(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Humanities-focused academic response with MLA citations
        params = self._get_valid_params()
        decorator = Academic(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Academic(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "academic")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Academic.from_dict(serialized)
        self.assertIsInstance(deserialized, Academic)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
