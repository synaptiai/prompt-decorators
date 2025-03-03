"""Tests for the Precision decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.precision import Precision


class TestPrecision(unittest.TestCase):
    """Tests for the Precision decorator.

    Enhances responses with exact, specific, and precisely defined information.
    This decorator prioritizes accuracy in measurements, terms, definitions, and
    claims, avoiding vague language in favor of concrete specificity.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "level": "moderate",
            "units": True,
            "definitions": False,
        }

    def test_validate_level(self):
        """Test validation for the level parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["level"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Precision(**params)
        self.assertIn("level", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["level"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Precision(**params)
        self.assertIn("level", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["level"] = "moderate"
        # This should not raise an exception
        Precision(**params)
        params["level"] = "high"
        # This should not raise an exception
        Precision(**params)
        params["level"] = "scientific"
        # This should not raise an exception
        Precision(**params)

    def test_validate_units(self):
        """Test validation for the units parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["units"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Precision(**params)
        self.assertIn("units", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_definitions(self):
        """Test validation for the definitions parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["definitions"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Precision(**params)
        self.assertIn("definitions", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic precise explanation of a scientific concept
        params = self._get_valid_params()
        decorator = Precision(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Highly precise response with scientific rigor
        params = self._get_valid_params()
        decorator = Precision(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Precision(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "precision")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Precision.from_dict(serialized)
        self.assertIsInstance(deserialized, Precision)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
