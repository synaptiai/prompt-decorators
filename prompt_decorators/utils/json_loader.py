"""
JSON Loader Module

This module provides utilities for loading decorator definitions from JSON.
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Type
import jsonschema

from prompt_decorators.core.base import BaseDecorator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class JSONLoader:
    """
    Loader for decorator definitions from JSON.
    
    This class provides utilities for loading decorator definitions from JSON strings,
    files, or directories, and validating them against a schema.
    """
    
    # Default schema file location
    DEFAULT_SCHEMA_PATH = Path(__file__).parent.parent.parent / "schemas" / "decorator.schema.json"
    
    def __init__(self, schema_path: Optional[str] = None):
        """
        Initialize the JSON loader.
        
        Args:
            schema_path: Path to the schema file for validation (optional)
        """
        self.schema_path = schema_path or str(self.DEFAULT_SCHEMA_PATH)
        self.schema = self._load_schema()
        
    def _load_schema(self) -> Dict[str, Any]:
        """
        Load the JSON schema for validation.
        
        Returns:
            The schema as a dictionary
            
        Raises:
            FileNotFoundError: If the schema file doesn't exist
            json.JSONDecodeError: If the schema is not valid JSON
        """
        try:
            schema_path = Path(self.schema_path)
            if not schema_path.exists():
                logger.warning(f"Schema file {schema_path} not found. Schema validation will be skipped.")
                return {}
                
            with open(schema_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading schema from {self.schema_path}: {e}")
            return {}
    
    def load_from_string(self, json_string: str, validate: bool = True) -> Dict[str, Any]:
        """
        Load a decorator definition from a JSON string.
        
        Args:
            json_string: The JSON string containing the decorator definition
            validate: Whether to validate against the schema
            
        Returns:
            The decorator definition as a dictionary
            
        Raises:
            json.JSONDecodeError: If the JSON is invalid
            jsonschema.exceptions.ValidationError: If validation fails
        """
        try:
            # Parse the JSON
            decorator_data = json.loads(json_string)
            
            # Validate against schema if requested and schema is available
            if validate and self.schema:
                self._validate_against_schema(decorator_data)
                
            return decorator_data
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON: {e}")
            raise
    
    def load_from_file(self, file_path: str, validate: bool = True) -> Dict[str, Any]:
        """
        Load a decorator definition from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            validate: Whether to validate against the schema
            
        Returns:
            The decorator definition as a dictionary
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the JSON is invalid
            jsonschema.exceptions.ValidationError: If validation fails
        """
        try:
            # Read the file
            with open(file_path, 'r') as f:
                json_string = f.read()
                
            # Parse and validate
            return self.load_from_string(json_string, validate)
        except FileNotFoundError as e:
            logger.error(f"File not found: {file_path}")
            raise
    
    def load_from_directory(self, directory_path: str, validate: bool = True) -> List[Dict[str, Any]]:
        """
        Load all decorator definitions from JSON files in a directory.
        
        Args:
            directory_path: Path to the directory containing JSON files
            validate: Whether to validate against the schema
            
        Returns:
            List of decorator definitions as dictionaries
        """
        decorators = []
        
        # Get all JSON files in the directory
        directory = Path(directory_path)
        if not directory.exists() or not directory.is_dir():
            logger.warning(f"Directory not found: {directory_path}")
            return decorators
            
        for file_path in directory.glob("**/*.json"):
            try:
                decorator_data = self.load_from_file(str(file_path), validate)
                decorator_data["_source_file"] = str(file_path)
                decorators.append(decorator_data)
            except (FileNotFoundError, json.JSONDecodeError, jsonschema.exceptions.ValidationError) as e:
                logger.warning(f"Error loading {file_path}: {e}")
                continue
                
        return decorators
    
    def _validate_against_schema(self, data: Dict[str, Any]) -> None:
        """
        Validate a decorator definition against the schema.
        
        Args:
            data: The decorator definition to validate
            
        Raises:
            jsonschema.exceptions.ValidationError: If validation fails
        """
        if not self.schema:
            logger.warning("Schema not available. Skipping validation.")
            return
            
        try:
            jsonschema.validate(instance=data, schema=self.schema)
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Schema validation failed: {e}")
            raise 