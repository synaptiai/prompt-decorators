"""Tests for the QualityMetrics decorator."""

import unittest
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators.generated.decorators.quality_metrics import QualityMetrics

class TestQualityMetrics(unittest.TestCase):
    """Tests for the QualityMetrics decorator.

    Applies specific quality measurements to evaluate content against defined
    criteria. This decorator enhances verification by providing quantifiable
    assessments of aspects like accuracy, completeness, clarity, or other custom
    metrics.

    """
    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "metrics": [],
            "scale": "1-5",
            "explanation": True,
        }

    def test_validate_metrics(self):
        """Test validation for the metrics parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['metrics'] = 'not_an_array'  # Not an array
        with self.assertRaises(ValidationError) as context:
            QualityMetrics(**params)
        self.assertIn('metrics', str(context.exception))
        self.assertIn('array', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_validate_scale(self):
        """Test validation for the scale parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['scale'] = 123  # Not a string
        with self.assertRaises(ValidationError) as context:
            QualityMetrics(**params)
        self.assertIn('scale', str(context.exception))
        self.assertIn('string', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test invalid enum value
        params['scale'] = 'invalid_enum_value'  # Invalid enum value
        with self.assertRaises(ValidationError) as context:
            QualityMetrics(**params)
        self.assertIn('scale', str(context.exception))
        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()

        # Test valid enum values
        params['scale'] = '1-5'
        # This should not raise an exception
        QualityMetrics(**params)
        params['scale'] = '1-10'
        # This should not raise an exception
        QualityMetrics(**params)
        params['scale'] = 'percentage'
        # This should not raise an exception
        QualityMetrics(**params)
        params['scale'] = 'qualitative'
        # This should not raise an exception
        QualityMetrics(**params)

    def test_validate_explanation(self):
        """Test validation for the explanation parameter."""
        # Get valid parameters
        params = self._get_valid_params()

        # Test type validation
        params['explanation'] = 'not_a_boolean'  # Not a boolean
        with self.assertRaises(ValidationError) as context:
            QualityMetrics(**params)
        self.assertIn('explanation', str(context.exception))
        self.assertIn('boolean', str(context.exception).lower())

        # Restore valid parameters
        params = self._get_valid_params()


    def test_apply_examples(self):
        """Test apply method with examples from the decorator definition."""
        # Basic quality assessment of an analysis
        params = self._get_valid_params()
        decorator = QualityMetrics(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # Specific custom metrics with detailed qualitative assessment
        params = self._get_valid_params()
        decorator = QualityMetrics(**params)
        result = decorator.apply("Sample prompt for testing.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


    def test_serialization(self):
        """Test serialization and deserialization."""
        # Create a decorator instance with valid parameters
        params = self._get_valid_params()
        decorator = QualityMetrics(**params)

        # Test to_dict() method
        serialized = decorator.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized["name"], "quality_metrics")
        self.assertIn("parameters", serialized)
        self.assertIsInstance(serialized["parameters"], dict)

        # Test that all parameters are included in the serialized output
        for param_name, param_value in params.items():
            self.assertIn(param_name, serialized["parameters"])

        # Test from_dict() method
        deserialized = QualityMetrics.from_dict(serialized)
        self.assertIsInstance(deserialized, QualityMetrics)

        # Test that the deserialized decorator has the same parameters
        deserialized_dict = deserialized.to_dict()
        self.assertEqual(serialized, deserialized_dict)