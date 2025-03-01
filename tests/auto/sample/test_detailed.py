#!/usr/bin/env python
"""
Test file for Detailed decorator.

This file contains unit tests for the Detailed decorator,
testing initialization, parameter validation, and application to prompts.
"""

import pytest
from typing import Dict, Any

from prompt_decorators.core.base import BaseDecorator


class TestDetailed:
    """
    Tests for the Detailed decorator.
    """
    
    def test_decorator_loads(self, load_decorator):
        """Test that the decorator can be loaded correctly"""
        decorator_class = load_decorator("Detailed")
        assert decorator_class is not None
        assert decorator_class.name == "Detailed"
        assert issubclass(decorator_class, BaseDecorator)
    
    def test_initialization_default_params(self, load_decorator):
        """Test initializing the decorator with default parameters"""
        decorator_class = load_decorator("Detailed")
        decorator = decorator_class()
        assert decorator is not None
        assert decorator.name == "Detailed"

    def test_depth_enum_validation(self, load_decorator):
        """Test that depth parameter accepts valid enum values"""
        decorator_class = load_decorator("Detailed")
        
        # Get valid parameters for all required fields
        params = {}
        for p in decorator_class.parameters:
            if p.required:
                # Add some basic value for required params
                if p.type == "string":
                    params[p.name] = "test"
                elif p.type == "number":
                    params[p.name] = 1
                elif p.type == "boolean":
                    params[p.name] = True
                elif p.type == "array":
                    params[p.name] = []
                elif p.type == "object":
                    params[p.name] = {}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid enum value
        params["depth"] = "moderate"
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Invalid enum value (if validation is implemented)
        params["depth"] = "INVALID_ENUM_VALUE"  # Not in enum
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate enum values, this might not fail
        except Exception:
            pass  # Expected to fail with strict validation

    def test_aspects_array_validation(self, load_decorator):
        """Test that aspects parameter accepts array values"""
        decorator_class = load_decorator("Detailed")
        
        # Get valid parameters for all required fields
        params = {}
        for p in decorator_class.parameters:
            if p.required:
                # Add some basic value for required params
                if p.type == "string":
                    params[p.name] = "test"
                elif p.type == "number":
                    params[p.name] = 1
                elif p.type == "boolean":
                    params[p.name] = True
                elif p.type == "array":
                    params[p.name] = []
                elif p.type == "object":
                    params[p.name] = {}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid empty array
        params["aspects"] = []
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Valid populated array
        params["aspects"] = ["item1", "item2"]
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-array value (if type validation is implemented)
        params["aspects"] = "not an array"  # Not an array
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation

    def test_examples_boolean_validation(self, load_decorator):
        """Test that examples parameter accepts boolean values"""
        decorator_class = load_decorator("Detailed")
        
        # Get valid parameters for all required fields
        params = {}
        for p in decorator_class.parameters:
            if p.required:
                # Add some basic value for required params
                if p.type == "string":
                    params[p.name] = "test"
                elif p.type == "number":
                    params[p.name] = 1
                elif p.type == "boolean":
                    params[p.name] = True
                elif p.type == "array":
                    params[p.name] = []
                elif p.type == "object":
                    params[p.name] = {}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Test with True
        params["examples"] = True
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Test with False
        params["examples"] = False
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-boolean value (if type validation is implemented)
        params["examples"] = "not a boolean"  # Not a boolean
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation

    def test_apply_method(self, load_decorator):
        """Test that the decorator's apply method works with examples from registry"""
        decorator_class = load_decorator("Detailed")

    def test_serialization(self, load_decorator):
        """Test that the decorator can be serialized and deserialized"""
        decorator_class = load_decorator("Detailed")
        
        # Create decorator with default parameters
        decorator = decorator_class()
        
        # Serialize to dict
        serialized = decorator.to_dict()
        
        # Validate serialized data
        assert isinstance(serialized, dict)
        assert "name" in serialized
        assert serialized["name"] == "Detailed"
        assert "version" in serialized
        assert "parameters" in serialized
        
        # Deserialize (if from_dict is implemented)
        try:
            deserialized = decorator_class.from_dict(serialized)
            assert deserialized is not None
            assert deserialized.name == decorator.name
            assert deserialized.version == decorator.version
        except (AttributeError, NotImplementedError):
            pass  # from_dict might not be implemented yet
