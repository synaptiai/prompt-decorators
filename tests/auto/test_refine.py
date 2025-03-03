"""Tests for the Refine decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.refine import Refine


class TestRefine(unittest.TestCase):
    """Tests for the Refine decorator.

    A meta-decorator that iteratively improves the output based on specified
    criteria or dimensions. This decorator simulates multiple drafts or
    revisions of content, with each iteration focusing on enhancing particular
    aspects of the response.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "iterations": 2,
            "focus": [],
            "showProcess": False,
        }

    def test_validate_iterations(self):
        """Test validation for the iterations parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["iterations"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Refine(**params)
        self.assertIn("iterations", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["iterations"] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Refine(**params)
        self.assertIn("iterations", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["iterations"] = 4  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Refine(**params)
        self.assertIn("iterations", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_focus(self):
        """Test validation for the focus parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["focus"] = "not_an_array"  # Not an array
        with self.assertRaises(ValidationError) as context:
            Refine(**params)
        self.assertIn("focus", str(context.exception))
        self.assertIn("array", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_showProcess(self):
        """Test validation for the showProcess parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["showProcess"] = "not_a_boolean"  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            Refine(**params)
        self.assertIn("showProcess", str(context.exception))
        self.assertIn("boolean", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic refinement of a complex explanation
        params = self._get_valid_params()
        decorator = Refine(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed refinement with visible iterations
        params = self._get_valid_params()
        decorator = Refine(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Refine(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "refine")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Refine.from_dict(serialized)
        self.assertIsInstance(deserialized, Refine)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
