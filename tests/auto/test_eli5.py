"""Tests for the ELI5 decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5

class TestELI5(unittest.TestCase):
    """Tests for the ELI5 decorator.

    Adapts the response to explain a concept as if to a 5-year-old child. This
    decorator simplifies complex topics using basic vocabulary, concrete
    examples, and relatable analogies to make information accessible to
    non-experts or those new to a subject.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "strictness": False,
        }

    def test_validate_strictness(self):
        """Test validation for the strictness parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['strictness'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            ELI5(**params)
        self.assertIn('strictness', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic explanation of a complex scientific concept
        params = self._get_valid_params()
        decorator = ELI5(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Strict simplified explanation of a technical subject
        params = self._get_valid_params()
        decorator = ELI5(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = ELI5(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "eli5")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = ELI5.from_dict(serialized)
        self.assertIsInstance(deserialized, ELI5)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)