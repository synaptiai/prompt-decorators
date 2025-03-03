"""Tests for the Contrarian decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.contrarian import Contrarian


class TestContrarian(unittest.TestCase):
    """Tests for the Contrarian decorator.

    Generates responses that deliberately challenge conventional wisdom or
    mainstream perspectives. This decorator encourages critical thinking by
    presenting counterarguments, alternative interpretations, or challenging
    established positions on a topic.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "approach": "outsider",
            "maintain": False,
            "focus": "example_value",
        }

    def test_validate_approach(self):
        """Test validation for the approach parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["approach"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Contrarian(**params)
        self.assertIn("approach", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["approach"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Contrarian(**params)
        self.assertIn("approach", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["approach"] = "outsider"
        # This should not raise an exception
        Contrarian(**params)
        params["approach"] = "skeptic"
        # This should not raise an exception
        Contrarian(**params)
        params["approach"] = "devils-advocate"
        # This should not raise an exception
        Contrarian(**params)

    def test_validate_maintain(self):
        """Test validation for the maintain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["maintain"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Contrarian(**params)
        self.assertIn("maintain", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["focus"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Contrarian(**params)
        self.assertIn("focus", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic devil's advocate approach with balanced conclusion
        params = self._get_valid_params()
        decorator = Contrarian(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Maintained skeptical contrarian stance focused on a specific aspect
        params = self._get_valid_params()
        decorator = Contrarian(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Contrarian(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "contrarian")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Contrarian.from_dict(serialized)
        self.assertIsInstance(deserialized, Contrarian)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
