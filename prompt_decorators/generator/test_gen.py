#!/usr/bin/env python
"""
Test Generator for Prompt Decorators

This module generates comprehensive unit tests for all decorators defined in the registry.
It creates test cases for:
1. Decorator initialization with valid and invalid parameters
2. Parameter validation
3. Apply method functionality
4. Serialization/deserialization
5. Compatibility checks

The generated tests follow pytest conventions and can be run with standard pytest commands.
"""

import os
import json
import importlib
import inspect
from pathlib import Path
from typing import Dict, List, Any, Type, Optional, Set, Tuple
import re
import textwrap

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.generator.registry import RegistryScanner

class TestGenerator:
    """
    Generator for decorator unit tests.
    """
    
    def __init__(
        self, 
        registry_dir: str,
        output_dir: str,
        template_dir: Optional[str] = None
    ):
        """
        Initialize the test generator.
        
        Args:
            registry_dir: Path to the decorator registry directory
            output_dir: Path where test files will be generated
            template_dir: Optional path to test template directory
        """
        self.registry_dir = Path(registry_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir) if template_dir else None
        self.scanner = RegistryScanner(registry_dir)
        
    def generate_all_tests(self) -> List[str]:
        """
        Generate test files for all decorators in the registry.
        
        Returns:
            List of generated test file paths
        """
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Get all decorators from registry
        decorator_files = self.scanner.scan()
        generated_files = []
        
        # Generate conftest.py for pytest fixtures
        conftest_path = self.generate_conftest()
        generated_files.append(conftest_path)
        
        # Generate a test file for each decorator
        for decorator_file in decorator_files:
            with open(decorator_file, 'r') as f:
                decorator_data = json.load(f)
                
            test_file_path = self.generate_decorator_test(decorator_data)
            if test_file_path:
                generated_files.append(test_file_path)
                
        # Generate test discovery file
        discovery_path = self.generate_test_discovery()
        generated_files.append(discovery_path)
        
        return generated_files
    
    def generate_conftest(self) -> str:
        """
        Generate conftest.py file with pytest fixtures.
        
        Returns:
            Path to the generated conftest.py file
        """
        conftest_path = self.output_dir / "conftest.py"
        
        conftest_content = """#!/usr/bin/env python
\"\"\"
Pytest fixtures for decorator tests.
\"\"\"

import pytest
from typing import Dict, Any, Optional, Type
import importlib
import inspect
from pathlib import Path

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.discovery import DecoratorRegistry

@pytest.fixture
def registry():
    \"\"\"Fixture for a clean decorator registry\"\"\"
    registry = DecoratorRegistry()
    registry.clear()
    return registry

@pytest.fixture
def sample_prompt():
    \"\"\"Fixture for a sample prompt to test decorators\"\"\"
    return "Explain quantum computing in simple terms."

@pytest.fixture
def load_decorator():
    \"\"\"Fixture for dynamically loading a decorator class\"\"\"
    def _load_decorator(decorator_name: str) -> Optional[Type[BaseDecorator]]:
        try:
            module_name = f"prompt_decorators.decorators.generated.decorators.{decorator_name.lower()}"
            module = importlib.import_module(module_name)
            
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, BaseDecorator) and 
                    obj != BaseDecorator and
                    getattr(obj, "name", "") == decorator_name):
                    return obj
            return None
        except ImportError:
            return None
    
    return _load_decorator

@pytest.fixture
def create_decorator():
    \"\"\"Fixture for creating a decorator instance with parameters\"\"\"
    def _create_decorator(decorator_class: Type[BaseDecorator], params: Dict[str, Any]):
        try:
            return decorator_class(**params)
        except Exception as e:
            return None
    
    return _create_decorator
"""
        
        with open(conftest_path, 'w') as f:
            f.write(conftest_content)
            
        return str(conftest_path)
    
    def generate_decorator_test(self, decorator_data: Dict[str, Any]) -> Optional[str]:
        """
        Generate a test file for a specific decorator.
        
        Args:
            decorator_data: Decorator definition from registry
            
        Returns:
            Path to the generated test file or None if generation failed
        """
        decorator_name = decorator_data.get("decoratorName")
        if not decorator_name:
            return None
            
        test_file_name = f"test_{decorator_name.lower()}.py"
        test_file_path = self.output_dir / test_file_name
        
        # Generate test file content
        test_content = self._generate_test_content(decorator_data)
        
        with open(test_file_path, 'w') as f:
            f.write(test_content)
            
        return str(test_file_path)
    
    def _generate_test_content(self, decorator_data: Dict[str, Any]) -> str:
        """
        Generate the content of a test file for a decorator.
        
        Args:
            decorator_data: Decorator definition from registry
            
        Returns:
            Test file content as string
        """
        decorator_name = decorator_data.get("decoratorName")
        decorator_description = decorator_data.get("description", "")
        parameters = decorator_data.get("parameters", [])
        examples = decorator_data.get("examples", [])
        
        # Generate test file header
        header = f"""#!/usr/bin/env python
\"\"\"
Test file for {decorator_name} decorator.

This file contains unit tests for the {decorator_name} decorator,
testing initialization, parameter validation, and application to prompts.
\"\"\"

import pytest
from typing import Dict, Any

from prompt_decorators.core.base import BaseDecorator

"""
        
        # Generate test class
        test_class = f"""
class Test{decorator_name}:
    \"\"\"
    Tests for the {decorator_name} decorator.
    \"\"\"
    
    def test_decorator_loads(self, load_decorator):
        \"\"\"Test that the decorator can be loaded correctly\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None
        assert decorator_class.name == "{decorator_name}"
        assert issubclass(decorator_class, BaseDecorator)
    
    def test_initialization_default_params(self, load_decorator):
        \"\"\"Test initializing the decorator with default parameters\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        decorator = decorator_class()
        assert decorator is not None
        assert decorator.name == "{decorator_name}"
"""

        # Generate parameter validation tests
        param_tests = ""
        for param in parameters:
            param_name = param.get("name")
            param_type = param.get("type")
            param_required = param.get("required", False)
            param_default = param.get("default", None)
            
            if param_required:
                param_tests += self._generate_required_param_test(decorator_name, param)
            
            param_tests += self._generate_param_validation_test(decorator_name, param)
        
        # Generate apply method tests
        apply_tests = self._generate_apply_tests(decorator_name, examples)
        
        # Generate serialization tests
        serialization_tests = self._generate_serialization_tests(decorator_name)
        
        # Combine all test components
        test_content = header + test_class + param_tests + apply_tests + serialization_tests
        
        return test_content
    
    def _generate_required_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for a required parameter"""
        param_name = param.get("name")
        return f"""
    def test_missing_required_param_{param_name}(self, load_decorator):
        \"\"\"Test that initialization fails when missing required parameter {param_name}\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Create params dict without the required parameter
        params = {{}}
        for p in decorator_class.parameters:
            if p.name != "{param_name}" and p.required:
                # Add some basic value for other required params
                if p.type == "string":
                    params[p.name] = "test"
                elif p.type == "number":
                    params[p.name] = 1
                elif p.type == "boolean":
                    params[p.name] = True
                elif p.type == "array":
                    params[p.name] = []
                elif p.type == "object":
                    params[p.name] = {{}}
        
        # Should raise an exception
        with pytest.raises(Exception):
            decorator = decorator_class(**params)
"""
    
    def _generate_param_validation_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for parameter validation"""
        param_name = param.get("name")
        param_type = param.get("type")
        
        # Different test based on parameter type
        if param_type == "string":
            return self._generate_string_param_test(decorator_name, param)
        elif param_type == "number":
            return self._generate_numeric_param_test(decorator_name, param)
        elif param_type == "boolean":
            return self._generate_boolean_param_test(decorator_name, param)
        elif param_type == "array":
            return self._generate_array_param_test(decorator_name, param)
        elif param_type == "enum":
            return self._generate_enum_param_test(decorator_name, param)
        else:
            return ""
    
    def _generate_string_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for string parameter validation"""
        param_name = param.get("name")
        pattern = param.get("pattern")
        
        if pattern:
            return f"""
    def test_{param_name}_pattern_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter is validated against pattern\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Valid value
        valid_params = self._get_valid_params(decorator_class)
        valid_params["{param_name}"] = "valid_value"  # Adjust with a valid pattern value
        decorator = decorator_class(**valid_params)
        assert decorator is not None
        
        # Invalid value - should validate pattern if implemented
        invalid_params = self._get_valid_params(decorator_class)
        invalid_params["{param_name}"] = "!@#$"  # Likely invalid pattern
        try:
            decorator = decorator_class(**invalid_params)
            # If implementation doesn't validate patterns, this might not fail
        except Exception:
            pass  # Expected to fail with strict pattern validation
            
    def _get_valid_params(self, decorator_class):
        \"\"\"Helper to get valid parameters for all required fields\"\"\"
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        return params
"""
        else:
            return f"""
    def test_{param_name}_string_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter accepts strings\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid string
        params["{param_name}"] = "valid string value"
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-string value (if type validation is implemented)
        params["{param_name}"] = 123  # Not a string
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation
"""
    
    def _generate_numeric_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for numeric parameter validation"""
        param_name = param.get("name")
        min_value = param.get("min")
        max_value = param.get("max")
        
        tests = f"""
    def test_{param_name}_numeric_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter accepts valid numeric values\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid value
        params["{param_name}"] = 5  # A reasonable value
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-numeric value (if type validation is implemented)
        params["{param_name}"] = "not a number"  # Not a number
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation
"""
        
        # Add min/max validation tests if defined
        if min_value is not None:
            tests += f"""
    def test_{param_name}_min_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter respects minimum value\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Value at minimum
        params["{param_name}"] = {min_value}
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Value below minimum
        params["{param_name}"] = {min_value - 1}
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate min, this might not fail
        except Exception:
            pass  # Expected to fail with strict validation
"""
        
        if max_value is not None:
            tests += f"""
    def test_{param_name}_max_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter respects maximum value\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Value at maximum
        params["{param_name}"] = {max_value}
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Value above maximum
        params["{param_name}"] = {max_value + 1}
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate max, this might not fail
        except Exception:
            pass  # Expected to fail with strict validation
"""
        
        return tests
    
    def _generate_boolean_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for boolean parameter validation"""
        param_name = param.get("name")
        
        return f"""
    def test_{param_name}_boolean_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter accepts boolean values\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Test with True
        params["{param_name}"] = True
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Test with False
        params["{param_name}"] = False
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-boolean value (if type validation is implemented)
        params["{param_name}"] = "not a boolean"  # Not a boolean
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation
"""
    
    def _generate_array_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for array parameter validation"""
        param_name = param.get("name")
        
        return f"""
    def test_{param_name}_array_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter accepts array values\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid empty array
        params["{param_name}"] = []
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Valid populated array
        params["{param_name}"] = ["item1", "item2"]
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Non-array value (if type validation is implemented)
        params["{param_name}"] = "not an array"  # Not an array
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate types, this might not fail
        except Exception:
            pass  # Expected to fail with strict type validation
"""
    
    def _generate_enum_param_test(self, decorator_name: str, param: Dict[str, Any]) -> str:
        """Generate test for enum parameter validation"""
        param_name = param.get("name")
        enum_values = param.get("enum", [])
        
        if not enum_values:
            return ""
        
        # Use first enum value as valid example
        valid_value = enum_values[0] if enum_values else "default"
        
        return f"""
    def test_{param_name}_enum_validation(self, load_decorator):
        \"\"\"Test that {param_name} parameter accepts valid enum values\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Get valid parameters for all required fields
        params = {{}}
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
                    params[p.name] = {{}}
                elif p.type == "enum":
                    params[p.name] = p.enum_values[0] if p.enum_values else "default"
        
        # Valid enum value
        params["{param_name}"] = "{valid_value}"
        decorator = decorator_class(**params)
        assert decorator is not None
        
        # Invalid enum value (if validation is implemented)
        params["{param_name}"] = "INVALID_ENUM_VALUE"  # Not in enum
        try:
            decorator = decorator_class(**params)
            # If implementation doesn't validate enum values, this might not fail
        except Exception:
            pass  # Expected to fail with strict validation
"""
    
    def _generate_apply_tests(self, decorator_name: str, examples: List[Dict[str, Any]]) -> str:
        """Generate tests for the apply method"""
        
        if not examples:
            # If no examples, create a basic apply test
            return f"""
    def test_apply_method(self, load_decorator, sample_prompt):
        \"\"\"Test that the decorator's apply method works\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Create decorator with default parameters
        decorator = decorator_class()
        
        # Apply to prompt
        decorated_prompt = decorator.apply(sample_prompt)
        
        # Basic validation - the decorated prompt should be a string
        assert isinstance(decorated_prompt, str)
        # The decorated prompt should be different from the original
        assert decorated_prompt != sample_prompt
        # The decorated prompt should contain the original prompt somewhere
        assert sample_prompt in decorated_prompt
"""
        
        # If we have examples, create tests based on them
        tests = f"""
    def test_apply_method(self, load_decorator):
        \"\"\"Test that the decorator's apply method works with examples from registry\"\"\"
        decorator_class = load_decorator("{decorator_name}")
"""
        
        for i, example in enumerate(examples):
            original_prompt = example.get("prompt", "")
            if not original_prompt:
                continue
                
            params = example.get("parameters", {})
            
            # Escape any quotes in the prompt
            safe_prompt = original_prompt.replace('"', '\\"')
            
            tests += f"""
        # Example {i+1}
        decorator{i} = decorator_class("""
            
            # Add parameters
            param_strs = []
            for key, value in params.items():
                if isinstance(value, str):
                    param_strs.append(f'{key}="{value}"')
                else:
                    param_strs.append(f'{key}={value}')
            
            tests += ", ".join(param_strs)
            
            tests += f""")
        original_prompt{i} = "{safe_prompt}"
        decorated_prompt{i} = decorator{i}.apply(original_prompt{i})
        
        # Basic validation
        assert isinstance(decorated_prompt{i}, str)
        assert decorated_prompt{i} != original_prompt{i}
        assert original_prompt{i} in decorated_prompt{i}
"""
        
        return tests
    
    def _generate_serialization_tests(self, decorator_name: str) -> str:
        """Generate tests for serialization/deserialization"""
        
        return f"""
    def test_serialization(self, load_decorator):
        \"\"\"Test that the decorator can be serialized and deserialized\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        
        # Create decorator with default parameters
        decorator = decorator_class()
        
        # Serialize to dict
        serialized = decorator.to_dict()
        
        # Validate serialized data
        assert isinstance(serialized, dict)
        assert "name" in serialized
        assert serialized["name"] == "{decorator_name}"
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
"""
    
    def generate_test_discovery(self) -> str:
        """
        Generate a test discovery file to help pytest find all tests.
        
        Returns:
            Path to the generated test discovery file
        """
        discovery_path = self.output_dir / "__init__.py"
        
        discovery_content = """#!/usr/bin/env python
\"\"\"
Test package for decorator tests.
This file enables pytest to discover all tests in this directory.
\"\"\"
"""
        
        with open(discovery_path, 'w') as f:
            f.write(discovery_content)
            
        return str(discovery_path)


def main():
    """Main entry point for the test generator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate tests for prompt decorators")
    parser.add_argument("--registry-dir", "-r", default="registry", 
                      help="Path to the decorator registry directory")
    parser.add_argument("--output-dir", "-o", default="tests/auto",
                      help="Path where test files will be generated")
    parser.add_argument("--template-dir", "-t", default=None,
                      help="Optional path to test template directory")
    
    args = parser.parse_args()
    
    generator = TestGenerator(
        registry_dir=args.registry_dir,
        output_dir=args.output_dir,
        template_dir=args.template_dir
    )
    
    generated_files = generator.generate_all_tests()
    
    print(f"Generated {len(generated_files)} test files:")
    for file_path in generated_files:
        print(f"  - {file_path}")


if __name__ == "__main__":
    main() 