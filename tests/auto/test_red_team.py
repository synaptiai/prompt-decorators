# Generated file - DO NOT EDIT BY HAND

import pytest
import json
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators import RedTeam


# Tests for the RedTeam decorator
# -------------------------------
class TestRedTeam:
    """Tests for the RedTeam decorator."""

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "strength": "moderate",
            "focus": [],
            "constructive": true,
        }

    def test_initialization_default_params(self, load_decorator):
        """Test initialization with default parameters."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        decorator = decorator_class()
        assert decorator is not None
        assert decorator.name == "RedTeam"

    def test_strength_type_validation(self, load_decorator):
        """Test strength type validation."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['strength'] = 'invalid_enum_value'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "strength" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_strength_enum_validation(self, load_decorator):
        """Test strength enum value validation."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['strength'] = 'invalid_enum_value'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "strength" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_focus_type_validation(self, load_decorator):
        """Test focus type validation."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['focus'] = 'invalid'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "focus" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_constructive_type_validation(self, load_decorator):
        """Test constructive type validation."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['constructive'] = 'invalid'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "constructive" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_apply_basic(self, load_decorator, sample_prompt):
        """Test basic apply functionality."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        decorator = decorator_class(**params)
        result = decorator.apply(sample_prompt)
        assert isinstance(result, str)

    def test_serialization(self, load_decorator):
        """Test decorator serialization."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        params = self._get_valid_params()
        decorator = decorator_class(**params)
        serialized = decorator.to_dict()
        assert isinstance(serialized, dict)
        assert serialized["name"] == decorator.name
        assert "parameters" in serialized
        assert isinstance(serialized["parameters"], dict)

    def test_version_compatibility(self, load_decorator):
        """Test version compatibility checks."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None

        # Test with current version
        current_version = decorator_class.version
        assert decorator_class.is_compatible_with_version(current_version)

        # Test with incompatible version
        with pytest.raises(IncompatibleVersionError):
            # Use a version lower than min_compatible_version to ensure incompatibility
            decorator_class.is_compatible_with_version("0.0.1")

        # Test instance method
        valid_params = self._get_valid_params()
        decorator = decorator_class(**valid_params)
        assert decorator.is_compatible_with_version(current_version)
        with pytest.raises(IncompatibleVersionError):
            # Use a version lower than min_compatible_version to ensure incompatibility
            decorator.is_compatible_with_version("0.0.1")

    def test_metadata(self, load_decorator):
        """Test decorator metadata."""
        decorator_class = load_decorator("RedTeam")
        assert decorator_class is not None
        metadata = decorator_class.get_metadata()
        assert isinstance(metadata, dict)
        assert metadata["name"] == "RedTeam"
        assert "description" in metadata
        assert "category" in metadata
        assert "version" in metadata
