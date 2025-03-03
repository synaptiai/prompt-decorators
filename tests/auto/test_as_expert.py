"""Tests for the AsExpert decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.as_expert import AsExpert

class TestAsExpert(unittest.TestCase):
    """Tests for the AsExpert decorator.

    Generates responses from the perspective of a specified domain expert or
    specialist. This decorator provides authoritative content that reflects the
    knowledge, terminology, and analytical approach of an expert in the
    specified field.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "domain": "example_value",
            "experience": "junior",
            "technical": True,
        }


    def test_missing_required_param_domain(self):
        """Test that initialization fails when missing required parameter domain."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "domain" in params:
            del params["domain"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            AsExpert(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "domain" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_domain(self):
        """Test validation for the domain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['domain'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            AsExpert(**params)
        self.assertIn('domain', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_experience(self):
        """Test validation for the experience parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['experience'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            AsExpert(**params)
        self.assertIn('experience', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['experience'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            AsExpert(**params)
        self.assertIn('experience', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['experience'] = 'junior'
        # This should not raise an exception
        AsExpert(**params)
        params['experience'] = 'senior'
        # This should not raise an exception
        AsExpert(**params)
        params['experience'] = 'leading'
        # This should not raise an exception
        AsExpert(**params)
        params['experience'] = 'pioneering'
        # This should not raise an exception
        AsExpert(**params)

    def test_validate_technical(self):
        """Test validation for the technical parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['technical'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            AsExpert(**params)
        self.assertIn('technical', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic response as a domain expert
        params = self._get_valid_params()
        decorator = AsExpert(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Highly technical response as pioneering expert
        params = self._get_valid_params()
        decorator = AsExpert(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = AsExpert(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "as_expert")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = AsExpert.from_dict(serialized)
        self.assertIsInstance(deserialized, AsExpert)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)