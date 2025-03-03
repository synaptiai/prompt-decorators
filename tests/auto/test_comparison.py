# Generated file - DO NOT EDIT BY HAND


import pytest

from prompt_decorators.core.base import ValidationError


# Tests for the Comparison decorator
# ----------------------------------
class TestComparison:
    """Tests for the Comparison decorator."""

    def _get_valid_params(self):
        """Get valid parameters for testing."""
        return {
            "aspects": [],
            "format": "table",
            "highlight": true,
        }

    def test_initialization_default_params(self, load_decorator):
        """Test initialization with default parameters."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        decorator = decorator_class()
        assert decorator is not None
        assert decorator.name == "Comparison"

    def test_aspects_type_validation(self, load_decorator):
        """Test aspects type validation."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        params = self._get_valid_params()
        params["aspects"] = "invalid"
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "aspects" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_format_type_validation(self, load_decorator):
        """Test format type validation."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        params = self._get_valid_params()
        params["format"] = "invalid_enum_value"
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "format" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_format_enum_validation(self, load_decorator):
        """Test format enum value validation."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        params = self._get_valid_params()
        params["format"] = "invalid_enum_value"
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "format" in str(exc_info.value)
        assert "one of" in str(exc_info.value).lower()

    def test_highlight_type_validation(self, load_decorator):
        """Test highlight type validation."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        params = self._get_valid_params()
        params["highlight"] = "invalid"
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "highlight" in str(exc_info.value)
        assert "type" in str(exc_info.value).lower()

    def test_apply_basic(self, load_decorator, sample_prompt):
        """Test basic apply functionality."""
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        params = self._get_valid_params()
        decorator = decorator_class(**params)
        result = decorator.apply(sample_prompt)
        assert isinstance(result, str)

    def test_serialization(self, load_decorator):
        """Test decorator serialization."""
        decorator_class = load_decorator("Comparison")
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
        decorator_class = load_decorator("Comparison")
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
        decorator_class = load_decorator("Comparison")
        assert decorator_class is not None
        metadata = decorator_class.get_metadata()
        assert isinstance(metadata, dict)
        assert metadata["name"] == "Comparison"
        assert "description" in metadata
        assert "category" in metadata
        assert "version" in metadata
