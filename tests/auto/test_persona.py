"""Tests for the Persona decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.persona import Persona

class TestPersona(unittest.TestCase):
    """Tests for the Persona decorator.

    Adapts the response to reflect the perspective and concerns of a specific
    persona. This decorator helps explore how different stakeholders or
    personality types would view a situation or topic.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "role": "example_value",
            "traits": [],
            "goals": [],
        }


    def test_missing_required_param_role(self):
        """Test that initialization fails when missing required parameter role."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "role" in params:
            del params["role"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            Persona(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "role" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_role(self):
        """Test validation for the role parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['role'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            Persona(**params)
        self.assertIn('role', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_traits(self):
        """Test validation for the traits parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['traits'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Persona(**params)
        self.assertIn('traits', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_goals(self):
        """Test validation for the goals parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['goals'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            Persona(**params)
        self.assertIn('goals', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Response from the perspective of a specific stakeholder
        params = self._get_valid_params()
        decorator = Persona(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed persona with specific traits and goals
        params = self._get_valid_params()
        decorator = Persona(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = Persona(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "persona")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = Persona.from_dict(serialized)
        self.assertIsInstance(deserialized, Persona)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)