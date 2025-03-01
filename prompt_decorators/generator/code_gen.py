"""
Code Generator Module

This module generates Python code from decorator definitions in the registry.
"""

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, Set, Tuple

from .registry import DecoratorData

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CodeGenerator:
    """Generator for Python code from decorator definitions."""
    
    def __init__(self, decorators: List[DecoratorData]):
        """
        Initialize the code generator.
        
        Args:
            decorators: List of decorator data dictionaries from the registry
        """
        self.decorators = decorators
        self.enum_definitions: Dict[str, Tuple[str, List[str]]] = {}  # Maps enum name to (description, values)
    
    def generate_all(self) -> Dict[str, str]:
        """
        Generate all Python files for the decorator package.
        
        Returns:
            Dictionary mapping file paths to generated code
        """
        result = {}
        
        # Generate decorator classes
        decorators_init = self._generate_decorators_init()
        result["decorators/__init__.py"] = decorators_init
        
        # Generate individual decorator files
        for decorator in self.decorators:
            file_name = self._get_decorator_file_name(decorator)
            code = self._generate_decorator_code(decorator)
            result[f"decorators/{file_name}"] = code
        
        # Generate enums module
        enums_code = self._generate_enums_module()
        result["decorators/enums.py"] = enums_code
        
        return result
    
    def _generate_decorators_init(self) -> str:
        """
        Generate the __init__.py file for the decorators package.
        
        Returns:
            Generated code as a string
        """
        code = [
            '"""',
            'Decorator Classes',
            '',
            'This package provides classes for all decorators in the Prompt Decorators specification.',
            '"""',
            '',
            '# Import all decorators',
        ]
        
        # Import statements for all decorators
        imports = []
        for decorator in self.decorators:
            name = decorator["decoratorName"]
            file_name = self._convert_to_snake_case(name)
            imports.append(f"from .{file_name} import {name}")
        
        code.extend(sorted(imports))
        
        # Export all decorators
        decorator_names = [decorator["decoratorName"] for decorator in self.decorators]
        code.append('')
        code.append('__all__ = [')
        for name in sorted(decorator_names):
            code.append(f'    "{name}",')
        code.append(']')
        
        return '\n'.join(code)
    
    def _generate_decorator_code(self, decorator: DecoratorData) -> str:
        """
        Generate Python code for a decorator class.
        
        Args:
            decorator: Decorator data dictionary
            
        Returns:
            Generated code as a string
        """
        name = decorator["decoratorName"]
        description = decorator.get("description", "")
        file_name = self._convert_to_snake_case(name)
        
        # Start with imports
        code = [
            '"""',
            f'{name} Decorator',
            '',
            f'{description}',
            '"""',
            '',
            'from typing import Dict, List, Optional, Any, Union, Literal',
            'from ..core.base import BaseDecorator',
        ]
        
        # Add enum imports if needed
        enums_to_import = self._get_enums_for_decorator(decorator)
        if enums_to_import:
            code.append('from .enums import ' + ', '.join(enums_to_import))
        
        code.append('')
        code.append('')
        
        # Generate class definition
        code.append(f'class {name}(BaseDecorator):')
        code.append(f'    """{description}"""')
        code.append('')
        
        # Generate __init__ method
        code.append('    def __init__(')
        code.append('        self,')
        
        # Add parameters to __init__ signature
        params = decorator.get("parameters", [])
        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param)
            
            if param.get("required", False):
                code.append(f'        {param_name}: {param_type},')
            else:
                default_value = self._get_default_value_str(param)
                if param_type.startswith('Optional['):
                    # Already Optional type
                    code.append(f'        {param_name}: {param_type} = {default_value},')
                else:
                    # Make it Optional
                    code.append(f'        {param_name}: Optional[{param_type}] = {default_value},')
        
        # Close init signature
        code.append('    ):')
        
        # Add docstring
        code.append('        """')
        code.append(f'        Initialize {name} decorator.')
        code.append('')
        code.append('        Args:')
        for param in params:
            param_name = param["name"]
            param_desc = param.get("description", "")
            code.append(f'            {param_name}: {param_desc}')
        code.append('        """')
        
        # Call super().__init__
        code.append('        super().__init__(')
        code.append(f'            name="{name}",')
        code.append(f'            version="{decorator["version"]}",')
        
        # Add parameters to super call
        code.append('            parameters={')
        for param in params:
            param_name = param["name"]
            code.append(f'                "{param_name}": {param_name},')
        code.append('            },')
        
        # Add metadata
        code.append('            metadata={')
        code.append(f'                "description": "{description}",')
        
        if "author" in decorator and "name" in decorator["author"]:
            code.append(f'                "author": "{decorator["author"]["name"]}",')
        
        # Add category if we can determine it
        if "_source_file" in decorator:
            parts = decorator["_source_file"].split('/')
            if len(parts) > 1:
                category = parts[0]
                code.append(f'                "category": "{category}",')
        
        code.append('            },')
        code.append('        )')
        
        # Add property getters for parameters
        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param)
            param_desc = param.get("description", "")
            
            code.append('')
            code.append('    @property')
            code.append(f'    def {param_name}(self) -> {param_type}:')
            code.append(f'        """{param_desc}"""')
            code.append(f'        return self.parameters.get("{param_name}")')
        
        # Add validation if needed
        has_validation = any('validation' in param for param in params)
        if has_validation:
            code.append('')
            code.append('    def validate(self) -> None:')
            code.append('        """Validate decorator parameters."""')
            code.append('        super().validate()')
            code.append('')
            
            for param in params:
                if 'validation' in param:
                    param_name = param["name"]
                    validation = param["validation"]
                    
                    if 'minimum' in validation:
                        code.append(f'        if self.{param_name} is not None and self.{param_name} < {validation["minimum"]}:')
                        code.append(f'            raise ValueError(f"{param_name} must be at least {validation["minimum"]}, got {{self.{param_name}}}")')
                    
                    if 'maximum' in validation:
                        code.append(f'        if self.{param_name} is not None and self.{param_name} > {validation["maximum"]}:')
                        code.append(f'            raise ValueError(f"{param_name} must be at most {validation["maximum"]}, got {{self.{param_name}}}")')
                    
                    if 'pattern' in validation:
                        pattern = validation["pattern"].replace('"', '\\"')
                        code.append(f'        if self.{param_name} is not None and not re.match(r"{pattern}", str(self.{param_name})):')
                        code.append(f'            raise ValueError(f"{param_name} must match pattern {pattern}, got {{self.{param_name}}}")')
        
        return '\n'.join(code)
    
    def _generate_enums_module(self) -> str:
        """
        Generate the enums.py module with all enum definitions.
        
        Returns:
            Generated code as a string
        """
        code = [
            '"""',
            'Decorator Enum Definitions',
            '',
            'This module provides enum types used by decorators.',
            '"""',
            '',
            'from enum import Enum',
            '',
        ]
        
        # Generate enums in alphabetical order
        for enum_name in sorted(self.enum_definitions.keys()):
            description, values = self.enum_definitions[enum_name]
            
            code.append('')
            code.append(f'class {enum_name}(str, Enum):')
            code.append(f'    """{description}"""')
            
            for value in values:
                constant_name = self._convert_to_enum_constant(value)
                code.append(f'    {constant_name} = "{value}"')
        
        return '\n'.join(code)
    
    def _collect_enums(self) -> None:
        """
        Collect all enum types from all decorators.
        """
        self.enum_definitions = {}
        
        for decorator in self.decorators:
            name = decorator["decoratorName"]
            
            for param in decorator.get("parameters", []):
                if param.get("type") == "enum" and "enum" in param:
                    param_name = param["name"]
                    enum_name = f"{name}{param_name.capitalize()}Enum"
                    description = param.get("description", f"Options for {name}.{param_name}")
                    values = param["enum"]
                    
                    self.enum_definitions[enum_name] = (description, values)
    
    def _get_enums_for_decorator(self, decorator: DecoratorData) -> List[str]:
        """
        Get list of enum types used by a decorator.
        
        Args:
            decorator: Decorator data
            
        Returns:
            List of enum class names
        """
        result = []
        name = decorator["decoratorName"]
        
        for param in decorator.get("parameters", []):
            if param.get("type") == "enum" and "enum" in param:
                param_name = param["name"]
                enum_name = f"{name}{param_name.capitalize()}Enum"
                
                # Ensure the enum exists in our definitions
                if enum_name not in self.enum_definitions:
                    description = param.get("description", f"Options for {name}.{param_name}")
                    values = param["enum"]
                    self.enum_definitions[enum_name] = (description, values)
                
                result.append(enum_name)
        
        return result
    
    def _get_python_type(self, param: Dict[str, Any]) -> str:
        """
        Convert parameter type to Python type annotation.
        
        Args:
            param: Parameter definition
            
        Returns:
            Python type annotation as string
        """
        param_type = param.get("type", "string")
        
        if param_type == "string":
            return "str"
        elif param_type == "number":
            return "float"
        elif param_type == "integer":
            return "int"
        elif param_type == "boolean":
            return "bool"
        elif param_type == "enum":
            # For enum types, reference the appropriate Enum class
            decorator_name = None
            param_name = param["name"]
            
            # Try to find the decorator this parameter belongs to
            for decorator in self.decorators:
                for p in decorator.get("parameters", []):
                    if p.get("name") == param_name and p.get("type") == "enum":
                        decorator_name = decorator["decoratorName"]
                        break
                if decorator_name:
                    break
            
            if decorator_name:
                return f"{decorator_name}{param_name.capitalize()}Enum"
            else:
                # Fallback to literal type if we can't determine the enum class
                if "enum" in param:
                    values = [self._format_literal_value(val) for val in param["enum"]]
                    return f"Literal[{', '.join(values)}]"
                return "str"
        elif param_type == "array":
            # If items type is specified, use that
            if "items" in param and "type" in param["items"]:
                item_type = self._get_python_type(param["items"])
                return f"List[{item_type}]"
            return "List[Any]"
        elif param_type == "object":
            return "Dict[str, Any]"
        else:
            return "Any"
    
    def _format_literal_value(self, value: Any) -> str:
        """
        Format a value for use in a Literal type.
        
        Args:
            value: Value to format
            
        Returns:
            Formatted value as string
        """
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return str(value)
    
    def _get_default_value_str(self, param: Dict[str, Any]) -> str:
        """
        Get string representation of default value for a parameter.
        
        Args:
            param: Parameter definition
            
        Returns:
            String representation of default value
        """
        if "default" not in param:
            return "None"
        
        default = param["default"]
        param_type = param.get("type", "string")
        
        if param_type == "string":
            return f'"{default}"'
        elif param_type == "boolean":
            return str(default).lower()
        elif param_type == "array":
            if not default:
                return "[]"
            # This is a simplification - would need more complex handling for non-primitive items
            items = [self._format_literal_value(item) for item in default]
            return f"[{', '.join(items)}]"
        elif param_type == "enum":
            # For enum types, reference the enum constant
            decorator_name = None
            param_name = param["name"]
            
            # Try to find the decorator this parameter belongs to
            for decorator in self.decorators:
                for p in decorator.get("parameters", []):
                    if p.get("name") == param_name and p.get("type") == "enum":
                        decorator_name = decorator["decoratorName"]
                        break
                if decorator_name:
                    break
            
            if decorator_name:
                enum_name = f"{decorator_name}{param_name.capitalize()}Enum"
                constant_name = self._convert_to_enum_constant(default)
                return f"{enum_name}.{constant_name}"
            else:
                return f'"{default}"'
        else:
            return str(default)
    
    def _convert_to_snake_case(self, name: str) -> str:
        """
        Convert camelCase or PascalCase to snake_case.
        
        Args:
            name: Name to convert
            
        Returns:
            snake_case version of the name
        """
        # Handle common acronyms that should stay together
        name = re.sub(r'JSON', 'Json', name)
        name = re.sub(r'XML', 'Xml', name)
        name = re.sub(r'YAML', 'Yaml', name)
        name = re.sub(r'HTML', 'Html', name)
        name = re.sub(r'CSS', 'Css', name)
        name = re.sub(r'URL', 'Url', name)
        name = re.sub(r'API', 'Api', name)
        
        # Convert camelCase to snake_case
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _convert_to_enum_constant(self, value: str) -> str:
        """
        Convert a string value to a valid enum constant name.
        
        Args:
            value: Value to convert
            
        Returns:
            Valid enum constant name
        """
        # Replace special characters with underscores
        result = re.sub(r'[^a-zA-Z0-9]', '_', str(value))
        
        # Convert to uppercase
        result = result.upper()
        
        # Ensure it starts with a letter
        if result and not result[0].isalpha():
            result = 'VALUE_' + result
        
        # Handle empty string
        if not result:
            result = 'EMPTY'
        
        return result
    
    def _get_decorator_file_name(self, decorator: DecoratorData) -> str:
        """
        Get the file name for a decorator module.
        
        Args:
            decorator: Decorator data
            
        Returns:
            File name (without directory)
        """
        name = decorator["decoratorName"]
        snake_case = self._convert_to_snake_case(name)
        return f"{snake_case}.py"


def generate_code(decorators: List[DecoratorData], output_dir: Optional[Union[str, Path]] = None) -> Dict[str, str]:
    """
    Generate Python code from decorator definitions.
    
    Args:
        decorators: List of decorator definitions
        output_dir: Optional output directory to write files to
        
    Returns:
        Dictionary mapping file paths to generated code
    """
    # Initialize the code generator
    generator = CodeGenerator(decorators)
    
    # Collect enum definitions
    generator._collect_enums()
    
    # Generate code
    generated_files = generator.generate_all()
    
    # Write to files if output_dir is specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for file_path, content in generated_files.items():
            full_path = output_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Generated {full_path}")
    
    return generated_files


if __name__ == "__main__":
    # Simple test when run directly
    import sys
    from .registry import scan_registry
    
    if len(sys.argv) > 1:
        registry_dir = sys.argv[1]
    else:
        # Default to registry directory relative to this file
        script_dir = Path(__file__).parent.parent.parent
        registry_dir = script_dir / "registry"
    
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = Path(__file__).parent.parent / "decorators" / "generated"
    
    print(f"Scanning registry at: {registry_dir}")
    print(f"Output directory: {output_dir}")
    
    try:
        # Scan registry
        decorators = scan_registry(registry_dir)
        
        # Generate code
        generate_code(decorators, output_dir)
        
        print(f"Generated {len(decorators)} decorator classes")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 