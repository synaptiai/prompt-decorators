"""Tests for the CiteSources decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.cite_sources import CiteSources


class TestCiteSources(unittest.TestCase):
    """Tests for the CiteSources decorator.

    Structures the response to include citations for claims and information.
    This decorator enhances credibility by providing references to source
    material, enabling fact verification and further exploration of topics.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "style": "inline",
            "format": "APA",
            "comprehensive": False,
        }

    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["style"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            CiteSources(**params)
        self.assertIn("style", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["style"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            CiteSources(**params)
        self.assertIn("style", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["style"] = "inline"
        # This should not raise an exception
        CiteSources(**params)
        params["style"] = "footnote"
        # This should not raise an exception
        CiteSources(**params)
        params["style"] = "endnote"
        # This should not raise an exception
        CiteSources(**params)

    def test_validate_format(self):
        """Test validation for the format parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["format"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            CiteSources(**params)
        self.assertIn("format", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["format"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            CiteSources(**params)
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
        CiteSources(**params)
        params["format"] = "MLA"
        # This should not raise an exception
        CiteSources(**params)
        params["format"] = "Chicago"
        # This should not raise an exception
        CiteSources(**params)
        params["format"] = "Harvard"
        # This should not raise an exception
        CiteSources(**params)
        params["format"] = "IEEE"
        # This should not raise an exception
        CiteSources(**params)

    def test_validate_comprehensive(self):
        """Test validation for the comprehensive parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["comprehensive"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            CiteSources(**params)
        self.assertIn("comprehensive", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic inline citations for a scientific topic
        params = self._get_valid_params()
        decorator = CiteSources(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Comprehensive footnote citations in Chicago style
        params = self._get_valid_params()
        decorator = CiteSources(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = CiteSources(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "cite_sources")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = CiteSources.from_dict(serialized)
        self.assertIsInstance(deserialized, CiteSources)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
