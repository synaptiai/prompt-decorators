"""Tests for the Narrative decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.narrative import Narrative


class TestNarrative(unittest.TestCase):
    """Tests for the Narrative decorator.

    Structures the response as a story-based delivery with narrative elements.
    This decorator employs storytelling techniques to make information more
    engaging, memorable, and contextually rich.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "structure": "classic",
            "characters": True,
            "length": "brief",
        }

    def test_validate_structure(self):
        """Test validation for the structure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["structure"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Narrative(**params)
        self.assertIn("structure", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["structure"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Narrative(**params)
        self.assertIn("structure", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["structure"] = "classic"
        # This should not raise an exception
        Narrative(**params)
        params["structure"] = "nonlinear"
        # This should not raise an exception
        Narrative(**params)
        params["structure"] = "case-study"
        # This should not raise an exception
        Narrative(**params)

    def test_validate_characters(self):
        """Test validation for the characters parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["characters"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Narrative(**params)
        self.assertIn("characters", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_length(self):
        """Test validation for the length parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["length"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Narrative(**params)
        self.assertIn("length", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["length"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Narrative(**params)
        self.assertIn("length", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["length"] = "brief"
        # This should not raise an exception
        Narrative(**params)
        params["length"] = "moderate"
        # This should not raise an exception
        Narrative(**params)
        params["length"] = "extended"
        # This should not raise an exception
        Narrative(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Classic narrative structure to explain a concept
        params = self._get_valid_params()
        decorator = Narrative(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Brief case study without character elements
        params = self._get_valid_params()
        decorator = Narrative(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Narrative(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "narrative")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Narrative.from_dict(serialized)
        self.assertIsInstance(deserialized, Narrative)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
