#!/usr/bin/env python3
"""
Test Generator for Prompt Decorators

This script automatically generates test files for prompt decorators based on their
JSON specifications. It creates unit tests for validating parameters, functional tests
based on examples, and integration tests for compatibility between decorators.
"""

import os
import json
import re
import glob
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
REGISTRY_PATH = "registry"
AUTO_TESTS_PATH = "tests/auto"
UTILS_PATH = "tests/utils"

def find_all_decorator_files(registry_path=REGISTRY_PATH):
    """Find all decorator JSON files in the registry."""
    return glob.glob(f"{registry_path}/**/*.json", recursive=True)

def load_decorator_json(file_path):
    """Load a decorator JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_category(file_path):
    """Extract category from file path."""
    parts = file_path.split(os.path.sep)
    if len(parts) >= 3 and parts[0] == 'registry':
        if parts[1] == 'core':
            return parts[2]
        return parts[1]
    return "misc"

def generate_test_header():
    """Generate standard test file header."""
    return '''"""
Automatically generated tests for prompt decorators.
DO NOT EDIT MANUALLY. Changes will be overwritten.
"""

import pytest
import re
import json
from tests.utils.test_helpers import (
    validate_decorator_in_prompt,
    check_expectation,
    LLMClient,
    combine_decorators,
    ValidationError,
)

# Initialize test client
llm_client = LLMClient(use_real_llm=False, use_cache=True)
'''

def generate_parameter_tests(decorator):
    """Generate tests for parameter validation."""
    tests = []
    decorator_name = decorator["decoratorName"]
    
    for param in decorator.get("parameters", []):
        param_name = param["name"]
        param_type = param["type"]
        required = param.get("required", False)
        
        # Test for required parameters
        if required:
            tests.append(f'''
def test_{decorator_name.lower()}_{param_name}_required():
    """Test that {param_name} is required for {decorator_name} decorator."""
    prompt = "+++{decorator_name}\\nTest prompt."
    with pytest.raises(ValidationError, match="{param_name}"):
        validate_decorator_in_prompt(prompt)
''')
        
        # Test for parameter type validation
        if param_type == "enum":
            valid_values = param.get("enum", [])
            if valid_values:
                enum_tests = []
                for val in valid_values:
                    enum_tests.append(f'validate_decorator_in_prompt("+++{decorator_name}({param_name}={val})\\nTest prompt.")')
                
                tests.append(f'''
def test_{decorator_name.lower()}_{param_name}_enum_values():
    """Test that {param_name} accepts only valid enum values."""
    # Valid values
    {'; '.join(enum_tests)}
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++{decorator_name}({param_name}=invalid_value)\\nTest prompt.")
''')
        
        # Number parameter type
        elif param_type == "number":
            min_val = param.get("validation", {}).get("minimum")
            max_val = param.get("validation", {}).get("maximum")
            
            if min_val is not None or max_val is not None:
                tests.append(f'''
def test_{decorator_name.lower()}_{param_name}_number_validation():
    """Test number validation for {param_name} parameter."""
    ''')
                
                if min_val is not None:
                    tests[-1] += f'''
    # Valid minimum value
    validate_decorator_in_prompt("+++{decorator_name}({param_name}={min_val})\\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++{decorator_name}({param_name}={min_val-1})\\nTest prompt.")
    '''
                
                if max_val is not None:
                    tests[-1] += f'''
    # Valid maximum value
    validate_decorator_in_prompt("+++{decorator_name}({param_name}={max_val})\\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++{decorator_name}({param_name}={max_val+1})\\nTest prompt.")
    '''
        
        # Boolean parameter type
        elif param_type == "boolean":
            tests.append(f'''
def test_{decorator_name.lower()}_{param_name}_boolean_validation():
    """Test boolean validation for {param_name} parameter."""
    # Test true value
    validate_decorator_in_prompt("+++{decorator_name}({param_name}=true)\\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++{decorator_name}({param_name}=false)\\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++{decorator_name}({param_name}=not_boolean)\\nTest prompt.")
''')
        
    return "\n".join(tests)

def extract_prompt_from_usage(usage):
    """Extract the actual prompt part from the usage example."""
    # Remove the decorator prefix
    parts = usage.split("\n", 1)
    if len(parts) > 1:
        return parts[1]
    return ""

def generate_expectation_checks(result_description):
    """Generate checks based on the expected result description."""
    expectations = []
    
    # Extract expectations from result description
    if re.search(r'bullet(ed|s|\s+point)', result_description.lower()):
        expectations.append('check_expectation(response, "contains_bullet_points")')
    
    if re.search(r'step[s]?\s+by\s+step', result_description.lower()) or re.search(r'numbered\s+steps', result_description.lower()):
        expectations.append('check_expectation(response, "contains_numbered_steps")')
    
    if 'concise' in result_description.lower() or 'brief' in result_description.lower():
        expectations.append('check_expectation(response, "is_concise")')
    
    if 'formal' in result_description.lower() or 'academic' in result_description.lower() or 'scholarly' in result_description.lower():
        expectations.append('check_expectation(response, "has_formal_language")')
    
    if 'table' in result_description.lower():
        expectations.append('check_expectation(response, "contains_table")')
    
    if 'json' in result_description.lower():
        expectations.append('check_expectation(response, "is_valid_json")')
    
    if 'markdown' in result_description.lower():
        expectations.append('check_expectation(response, "is_valid_markdown")')
    
    if re.search(r'compar(e|ison|ing)', result_description.lower()):
        expectations.append('check_expectation(response, "contains_comparison")')
    
    if 'pros and cons' in result_description.lower() or 'advantages and disadvantages' in result_description.lower():
        expectations.append('check_expectation(response, "contains_pros_and_cons")')
    
    # If no specific expectations were identified, add a generic check
    if not expectations:
        expectations.append('check_expectation(response, "matches_description", description="' + result_description.replace('"', '\\"') + '")')
    
    return expectations

def generate_example_tests(decorator):
    """Generate tests based on the examples in the decorator."""
    tests = []
    decorator_name = decorator["decoratorName"]
    
    for i, example in enumerate(decorator.get("examples", [])):
        usage = example.get("usage", "")
        expected_result = example.get("result", "")
        description = example.get("description", "")
        
        if not usage or not expected_result:
            continue
        
        # Generate safe test name
        test_name = re.sub(r'[^a-zA-Z0-9_]', '_', description.lower())
        if not test_name:
            test_name = f"example_{i+1}"
        
        # Escape special characters in usage
        escaped_usage = usage.replace('"', '\\"').replace('\n', '\\n')
        
        # Generate expectations
        expectations = generate_expectation_checks(expected_result)
        expectations_code = '\n    '.join(expectations)
        
        tests.append(f'''
def test_{decorator_name.lower()}_{test_name}():
    """Test {decorator_name} with example: {description}"""
    response = llm_client.generate("{escaped_usage}")
    
    # Check if response meets expectations
    {expectations_code}
''')
    
    return "\n".join(tests)

def generate_compatibility_tests(decorator):
    """Generate compatibility tests for a decorator."""
    tests = []
    decorator_name = decorator["decoratorName"]
    compatibility = decorator.get("compatibility", {})
    
    # Test for conflicts
    conflicts = compatibility.get("conflicts", [])
    if conflicts:
        conflict_list = ", ".join([f'"{c}"' for c in conflicts])
        tests.append(f'''
def test_{decorator_name.lower()}_conflicts():
    """Test that {decorator_name} has expected conflicts."""
    conflicts = [{conflict_list}]
    for conflict in conflicts:
        result = combine_decorators(["{decorator_name}", conflict])
        assert not result["compatible"], f"{decorator_name} should conflict with {{conflict}}"
''')
    
    # Test for required decorators
    requires = compatibility.get("requires", [])
    if requires:
        require_list = ", ".join([f'"{r}"' for r in requires])
        tests.append(f'''
def test_{decorator_name.lower()}_requirements():
    """Test that {decorator_name} has expected requirements."""
    requirements = [{require_list}]
    for requirement in requirements:
        # Test without the required decorator
        result = validate_decorator_in_prompt("+++{decorator_name}\\nTest prompt.")
        assert not result["valid"], f"{decorator_name} should require {{requirement}}"
        
        # Test with the required decorator
        result = validate_decorator_in_prompt("+++{{requirement}}\\n+++{decorator_name}\\nTest prompt.")
        assert result["valid"], f"{decorator_name} should work with {{requirement}}"
''')
    
    return "\n".join(tests)

def generate_decorator_test_file(decorator, category):
    """Generate a complete test file for a decorator."""
    decorator_name = decorator["decoratorName"]
    
    content = [
        generate_test_header(),
        f"\n# Tests for {decorator_name} decorator",
        "\n# Parameter validation tests",
        generate_parameter_tests(decorator),
        "\n# Example-based tests",
        generate_example_tests(decorator),
        "\n# Compatibility tests",
        generate_compatibility_tests(decorator)
    ]
    
    return "\n".join(content)

def generate_test_helpers():
    """Generate test helper functions."""
    # We already have a comprehensive test_helpers.py, so we'll use that instead
    return """
"""
    
def main():
    """Main entry point for test generation."""
    # Create directory structure
    os.makedirs(AUTO_TESTS_PATH, exist_ok=True)
    os.makedirs(UTILS_PATH, exist_ok=True)
    
    # Find all decorator files
    decorator_files = find_all_decorator_files()
    logger.info(f"Found {len(decorator_files)} decorator files.")
    
    # Process each decorator
    for file_path in decorator_files:
        try:
            decorator = load_decorator_json(file_path)
            category = extract_category(file_path)
            
            # Create category directory
            category_dir = os.path.join(AUTO_TESTS_PATH, category)
            os.makedirs(category_dir, exist_ok=True)
            
            # Generate test file
            test_content = generate_decorator_test_file(decorator, category)
            
            # Write test file
            decorator_name = decorator["decoratorName"].lower()
            test_file_path = os.path.join(category_dir, f"{decorator_name}_test.py")
            with open(test_file_path, 'w') as f:
                f.write(test_content)
            
            logger.info(f"Generated tests for {decorator['decoratorName']} in {test_file_path}")
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
    
    # Don't overwrite existing test_helpers.py if it already exists
    helper_path = os.path.join(UTILS_PATH, "test_helpers.py")
    if not os.path.exists(helper_path):
        with open(helper_path, 'w') as f:
            f.write(generate_test_helpers())
    
    logger.info(f"Test generation complete. Tests written to {AUTO_TESTS_PATH}")

if __name__ == "__main__":
    main() 