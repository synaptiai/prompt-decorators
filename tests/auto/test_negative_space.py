"""Tests for the NegativeSpace decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.negative_space import (
    NegativeSpace,
)


class TestNegativeSpace(unittest.TestCase):
    """Tests for the NegativeSpace decorator.

    Focuses on analyzing what is not explicitly stated, implied, or missing from
    a topic or question. This decorator explores the 'negative space' by
    identifying unexplored angles, implicit assumptions, unasked questions, and
    contextual elements that may have been overlooked.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "focus": "implications",
            "depth": "surface",
            "structure": "before",
        }

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["focus"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("focus", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["focus"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("focus", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["focus"] = "implications"
        # This should not raise an exception
        NegativeSpace(**params)
        params["focus"] = "missing"
        # This should not raise an exception
        NegativeSpace(**params)
        params["focus"] = "unstated"
        # This should not raise an exception
        NegativeSpace(**params)
        params["focus"] = "comprehensive"
        # This should not raise an exception
        NegativeSpace(**params)

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["depth"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("depth", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["depth"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("depth", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["depth"] = "surface"
        # This should not raise an exception
        NegativeSpace(**params)
        params["depth"] = "moderate"
        # This should not raise an exception
        NegativeSpace(**params)
        params["depth"] = "deep"
        # This should not raise an exception
        NegativeSpace(**params)

    def test_validate_structure(self):
        """Test validation for the structure parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["structure"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("structure", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["structure"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            NegativeSpace(**params)
        self.assertIn("structure", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["structure"] = "before"
        # This should not raise an exception
        NegativeSpace(**params)
        params["structure"] = "after"
        # This should not raise an exception
        NegativeSpace(**params)
        params["structure"] = "integrated"
        # This should not raise an exception
        NegativeSpace(**params)
        params["structure"] = "separate"
        # This should not raise an exception
        NegativeSpace(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic comprehensive negative space analysis
        params = self._get_valid_params()
        decorator = NegativeSpace(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Deep negative space analysis focused on missing elements
        params = self._get_valid_params()
        decorator = NegativeSpace(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = NegativeSpace(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "negative_space")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = NegativeSpace.from_dict(serialized)
        self.assertIsInstance(deserialized, NegativeSpace)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
