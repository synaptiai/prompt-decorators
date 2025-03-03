"""Tests for the Professional decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.professional import Professional

class TestProfessional(unittest.TestCase):
    """Tests for the Professional decorator.

    Adapts the response to use business-oriented language appropriate for
    professional contexts. This decorator generates content using formal
    business terminology, clear and concise phrasing, and industry-appropriate
    jargon when relevant.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "industry": "general",
            "formality": "standard",
        }

    def test_validate_industry(self):
        """Test validation for the industry parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['industry'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Professional(**params)
        self.assertIn('industry', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_formality(self):
        """Test validation for the formality parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['formality'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Professional(**params)
        self.assertIn('formality', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['formality'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            Professional(**params)
        self.assertIn('formality', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['formality'] = 'standard'
        # This should not raise an exception
        Professional(**params)
        params['formality'] = 'high'
        # This should not raise an exception
        Professional(**params)
        params['formality'] = 'executive'
        # This should not raise an exception
        Professional(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Standard professional business communication
        params = self._get_valid_params()
        decorator = Professional(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Industry-specific executive-level communication
        params = self._get_valid_params()
        decorator = Professional(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Professional(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "professional")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Professional.from_dict(serialized)
        self.assertIsInstance(deserialized, Professional)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)