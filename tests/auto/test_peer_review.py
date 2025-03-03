"""Tests for the PeerReview decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.peer_review import PeerReview

class TestPeerReview(unittest.TestCase):
    """Tests for the PeerReview decorator.

    Augments the response with a simulated peer review of the content. This
    decorator enhances critical thinking by evaluating the response's strengths,
    weaknesses, methodological soundness, and potential improvements as an
    academic reviewer would.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "criteria": "accuracy",
            "style": "constructive",
            "position": "after",
        }

    def test_validate_criteria(self):
        """Test validation for the criteria parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['criteria'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('criteria', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['criteria'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('criteria', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['criteria'] = 'accuracy'
        # This should not raise an exception
        PeerReview(**params)
        params['criteria'] = 'methodology'
        # This should not raise an exception
        PeerReview(**params)
        params['criteria'] = 'limitations'
        # This should not raise an exception
        PeerReview(**params)
        params['criteria'] = 'completeness'
        # This should not raise an exception
        PeerReview(**params)
        params['criteria'] = 'all'
        # This should not raise an exception
        PeerReview(**params)

    def test_validate_style(self):
        """Test validation for the style parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['style'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('style', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['style'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('style', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['style'] = 'constructive'
        # This should not raise an exception
        PeerReview(**params)
        params['style'] = 'critical'
        # This should not raise an exception
        PeerReview(**params)
        params['style'] = 'balanced'
        # This should not raise an exception
        PeerReview(**params)

    def test_validate_position(self):
        """Test validation for the position parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['position'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('position', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['position'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            PeerReview(**params)
        self.assertIn('position', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['position'] = 'after'
        # This should not raise an exception
        PeerReview(**params)
        params['position'] = 'before'
        # This should not raise an exception
        PeerReview(**params)
        params['position'] = 'alongside'
        # This should not raise an exception
        PeerReview(**params)

    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic peer review of content accuracy
        params = self._get_valid_params()
        decorator = PeerReview(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Critical peer review of multiple aspects, shown alongside content
        params = self._get_valid_params()
        decorator = PeerReview(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = PeerReview(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "peer_review")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = PeerReview.from_dict(serialized)
        self.assertIsInstance(deserialized, PeerReview)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)