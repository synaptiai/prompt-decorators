"""Tests for the RootCause decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.root_cause import RootCause


class TestRootCause(unittest.TestCase):
    """Tests for the RootCause decorator.

    Structures the response to systematically analyze underlying causes of
    problems or situations. This decorator applies formal root cause analysis
    methodologies to identify fundamental factors rather than just symptoms or
    immediate causes.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "method": "fivewhys",
            "depth": 5,
        }

    def test_validate_method(self):
        """Test validation for the method parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["method"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            RootCause(**params)
        self.assertIn("method", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["method"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            RootCause(**params)
        self.assertIn("method", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["method"] = "fivewhys"
        # This should not raise an exception
        RootCause(**params)
        params["method"] = "fishbone"
        # This should not raise an exception
        RootCause(**params)
        params["method"] = "pareto"
        # This should not raise an exception
        RootCause(**params)

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["depth"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            RootCause(**params)
        self.assertIn("depth", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["depth"] = 2  # Below minimum
        with self.assertRaises(ValidationError) as context:
            RootCause(**params)
        self.assertIn("depth", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["depth"] = 8  # Above maximum
        with self.assertRaises(ValidationError) as context:
            RootCause(**params)
        self.assertIn("depth", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic 5 Whys analysis of a business problem
        params = self._get_valid_params()
        decorator = RootCause(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Fishbone diagram approach to a technical issue
        params = self._get_valid_params()
        decorator = RootCause(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Pareto analysis with deeper investigation
        params = self._get_valid_params()
        decorator = RootCause(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = RootCause(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "root_cause")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = RootCause.from_dict(serialized)
        self.assertIsInstance(deserialized, RootCause)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
