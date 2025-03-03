# Generated file - DO NOT EDIT BY HAND

import pytest
import json
from prompt_decorators.core.base import ValidationError
from prompt_decorators.decorators import Priority


# Tests for the Priority decorator
# --------------------------------
class TestPriority:
    """Tests for the Priority decorator."""

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "decorators": [],
            "explicit": false,
            "mode": "override",
        }

    def test_initialization_default_params(self, load_decorator):
        """Test initialization with default parameters."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        decorator = decorator_class(**params)
        assert decorator is not None
        assert decorator.name == "Priority"

    def test_decorators_required(self, load_decorator):
        """Test that decorators is required."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        del params["decorators"]
        with pytest.raises(ValidationError):
            decorator_class(**params)

    def test_decorators_type_validation(self, load_decorator):
        """Test decorators type validation."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['decorators'] = 'invalid'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "decorators" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_explicit_type_validation(self, load_decorator):
        """Test explicit type validation."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['explicit'] = 'invalid'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "explicit" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_mode_type_validation(self, load_decorator):
        """Test mode type validation."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['mode'] = 'invalid_enum_value'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "mode" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_mode_enum_validation(self, load_decorator):
        """Test mode enum value validation."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        params['mode'] = 'invalid_enum_value'
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "mode" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_apply_basic(self, load_decorator, sample_prompt):
        """Test basic apply functionality."""
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        params = self._get_valid_params()
        decorator = decorator_class(**params)
        result = decorator.apply(sample_prompt)
        assert isinstance(result, str)

    def test_serialization(self, load_decorator):
        """Test decorator serialization."""
        decorator_class = load_decorator("Priority")
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
        decorator_class = load_decorator("Priority")
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
        decorator_class = load_decorator("Priority")
        assert decorator_class is not None
        metadata = decorator_class.get_metadata()
        assert isinstance(metadata, dict)
        assert metadata["name"] == "Priority"
        assert "description" in metadata
        assert "category" in metadata
        assert "version" in metadata
