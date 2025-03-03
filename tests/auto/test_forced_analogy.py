"""Tests for the ForcedAnalogy decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.forced_analogy import ForcedAnalogy

class TestForcedAnalogy(unittest.TestCase):
    """Tests for the ForcedAnalogy decorator.

    Explains concepts by specifically comparing them to a particular domain or
    field. This decorator forces analogies from a specified source domain to
    make complex or unfamiliar topics more relatable and understandable.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "source": "example_value",
            "comprehensiveness": "basic",
            "mappings": 3,
        }


    def test_missing_required_param_source(self):
        """Test that initialization fails when missing required parameter source."""
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "source" in params:
            del params["source"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            ForcedAnalogy(**params)
        
        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "source" in error_message or 
            "required" in error_message.lower()
        )


    def test_validate_source(self):
        """Test validation for the source parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['source'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('source', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_comprehensiveness(self):
        """Test validation for the comprehensiveness parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['comprehensiveness'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('comprehensiveness', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['comprehensiveness'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('comprehensiveness', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['comprehensiveness'] = 'basic'
        # This should not raise an exception
        ForcedAnalogy(**params)
        params['comprehensiveness'] = 'comprehensive'
        # This should not raise an exception
        ForcedAnalogy(**params)
        params['comprehensiveness'] = 'detailed'
        # This should not raise an exception
        ForcedAnalogy(**params)

    def test_validate_mappings(self):
        """Test validation for the mappings parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['mappings'] = 'not_a_number'  # Not a number
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('mappings', str(context.exception))
        self.assertIn('numeric', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test minimum value validation
        params['mappings'] = 0  # Below minimum
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('mappings', str(context.exception))
        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test maximum value validation
        params['mappings'] = 8  # Above maximum
        with self.assertRaises(ValidationError) as context:
            ForcedAnalogy(**params)
        self.assertIn('mappings', str(context.exception))
        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Explaining a technical concept using sports analogies
        params = self._get_valid_params()
        decorator = ForcedAnalogy(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Detailed cooking analogy for complex scientific process
        params = self._get_valid_params()
        decorator = ForcedAnalogy(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = ForcedAnalogy(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "forced_analogy")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = ForcedAnalogy.from_dict(serialized)
        self.assertIsInstance(deserialized, ForcedAnalogy)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)