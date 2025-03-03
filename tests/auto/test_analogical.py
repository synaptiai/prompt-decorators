"""Tests for the Analogical decorator."""

import unittest

from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.analogical import Analogical


class TestAnalogical(unittest.TestCase):
    """Tests for the Analogical decorator.

    Enhances explanations through the use of analogies and metaphors. This
    decorator helps make complex or abstract concepts more accessible by
    systematically comparing them to more familiar domains or experiences.

    """

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "domain": "general",
            "count": 1,
            "depth": "brief",
        }

    def test_validate_domain(self):
        """Test validation for the domain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["domain"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("domain", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_count(self):
        """Test validation for the count parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["count"] = "not_a_number"  # Not a number
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("count", str(context.exception))
        self.assertIn("numeric", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params["count"] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "minimum" in str(context.exception).lower()
            or "greater than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params["count"] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("count", str(context.exception))
        self.assertTrue(
            "maximum" in str(context.exception).lower()
            or "less than" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

    def test_validate_depth(self):
        """Test validation for the depth parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params["depth"] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("depth", str(context.exception))
        self.assertIn("string", str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params["depth"] = "invalid_enum_value"  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Analogical(**params)
        self.assertIn("depth", str(context.exception))
        self.assertTrue(
            "must be one of" in str(context.exception).lower()
            or "valid options" in str(context.exception).lower()
            or "enum" in str(context.exception).lower()
        )

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params["depth"] = "brief"
        # This should not raise an exception
        Analogical(**params)
        params["depth"] = "moderate"
        # This should not raise an exception
        Analogical(**params)
        params["depth"] = "extended"
        # This should not raise an exception
        Analogical(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Single analogy from a specific domain
        params = self._get_valid_params()
        decorator = Analogical(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Multiple brief analogies from different domains
        params = self._get_valid_params()
        decorator = Analogical(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Analogical(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "analogical")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Analogical.from_dict(serialized)
        self.assertIsInstance(deserialized, Analogical)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)
