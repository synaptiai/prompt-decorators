"""Tests for the StressTest decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.stress_test import StressTest

class TestStressTest(unittest.TestCase):
    """Tests for the StressTest decorator.

    Tests the robustness of ideas, theories, plans, or systems by applying
    extreme conditions, edge cases, and unlikely scenarios. This decorator helps
    identify vulnerabilities, limitations, and breaking points that might not be
    apparent under normal circumstances.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "scenarios": 3,
            "severity": "moderate",
            "domain": "example_value",
        }

    def test_validate_scenarios(self):
        """Test validation for the scenarios parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['scenarios'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('scenarios', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['scenarios'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('scenarios', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['scenarios'] = 6  # Above maximum
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('scenarios', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_severity(self):
        """Test validation for the severity parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['severity'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('severity', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['severity'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('severity', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['severity'] = 'moderate'
        # This should not raise an exception
        StressTest(**params)
        params['severity'] = 'severe'
        # This should not raise an exception
        StressTest(**params)
        params['severity'] = 'extreme'
        # This should not raise an exception
        StressTest(**params)

    def test_validate_domain(self):
        """Test validation for the domain parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['domain'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            StressTest(**params)
        self.assertIn('domain', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic stress test of a business model
        params = self._get_valid_params()
        decorator = StressTest(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Extreme stress test focused on a specific domain
        params = self._get_valid_params()
        decorator = StressTest(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = StressTest(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "stress_test")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = StressTest.from_dict(serialized)
        self.assertIsInstance(deserialized, StressTest)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)