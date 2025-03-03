"""JSON loading utilities for decorator definitions.

This module provides utilities for loading and validating decorator definitions from JSON.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import jsonschema

# Configure logging
logger = logging.getLogger(__name__)


class JSONLoader:
    """Loader for decorator definitions from JSON.

    This class provides utilities for loading decorator definitions from JSON strings,
    files, or directories, and validating them against a schema.
    """

    # Default schema file location
    DEFAULT_SCHEMA_PATH = (
        Path(__file__).parent.parent / "schemas" / "decorator_schema.json"
    )

    def __init__(self, schema_path: Optional[str] = None):
        """Initialize the JSON loader.

        Args:
            schema_path: Path to the schema file for validation (optional)
        """
        self.schema_path = schema_path or str(self.DEFAULT_SCHEMA_PATH)
        self.schema = self._load_schema()

    def _load_schema(self) -> Dict[str, Any]:
        """Load the JSON schema for validation.

        Args:
            self: The loader instance

        Returns:
            The loaded schema as a dictionary

        Raises:
            FileNotFoundError: If the schema file is not found
            json.JSONDecodeError: If the schema file contains invalid JSON
        """
        try:
            schema_path = Path(self.schema_path)
            if not schema_path.exists():
                logger.warning(f"Schema file not found: {schema_path}")
                return {}

            with open(schema_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid schema JSON: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error loading schema: {e}")
            return {}

    def load_from_string(
        self, json_string: str, validate: bool = True
    ) -> Dict[str, Any]:
        """Load a decorator definition from a JSON string.

        Args:
            json_string: The JSON string to load
            validate: Whether to validate against the schema (default: True)

        Returns:
            The decorator definition as a dictionary

        Raises:
            json.JSONDecodeError: If the JSON is invalid
            jsonschema.exceptions.ValidationError: If validation fails
        """
        try:
            # Parse the JSON
            decorator_data = json.loads(json_string)

            # Validate if requested
            if validate:
                self._validate_against_schema(decorator_data)

            return decorator_data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            raise
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading JSON: {e}")
            raise

    def load_from_file(self, file_path: str, validate: bool = True) -> Dict[str, Any]:
        """Load a decorator definition from a JSON file.

        Args:
            file_path: Path to the JSON file
            validate: Whether to validate against the schema (default: True)

        Returns:
            The decorator definition as a dictionary

        Raises:
            FileNotFoundError: If the file is not found
            json.JSONDecodeError: If the JSON is invalid
            jsonschema.exceptions.ValidationError: If validation fails
        """
        try:
            # Read the file
            with open(file_path, "r") as f:
                json_string = f.read()

            # Load from the string
            return self.load_from_string(json_string, validate)
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading from file {file_path}: {e}")
            raise

    def load_from_directory(
        self, directory_path: str, validate: bool = True
    ) -> List[Dict[str, Any]]:
        """Load all decorator definitions from JSON files in a directory.

        Args:
            directory_path: Path to the directory containing JSON files
            validate: Whether to validate against the schema (default: True)

        Returns:
            List of decorator definitions as dictionaries
        """
        decorators = []

        # Get all JSON files in the directory
        try:
            directory = Path(directory_path)
            if not directory.exists() or not directory.is_dir():
                logger.warning(f"Directory not found: {directory_path}")
                return []

            for file_path in directory.glob("**/*.json"):
                try:
                    decorator = self.load_from_file(str(file_path), validate)
                    decorators.append(decorator)
                except Exception as e:
                    logger.warning(f"Error loading {file_path}: {e}")
                    continue
        except Exception as e:
            logger.error(f"Error scanning directory {directory_path}: {e}")

        return decorators

    def _validate_against_schema(self, data: Dict[str, Any]) -> None:
        """Validate a decorator definition against the schema.

        Args:
            data: The decorator definition to validate

        Returns:
            None

        Raises:
            jsonschema.exceptions.ValidationError: If validation fails
        """
        if not self.schema:
            logger.warning("Schema not available. Skipping validation.")
            return

        jsonschema.validate(instance=data, schema=self.schema)


# Helper function to load a JSON file
def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        The loaded JSON data as a dictionary

    Raises:
        FileNotFoundError: If the file is not found
        json.JSONDecodeError: If the JSON is invalid
    """
    with open(file_path, "r") as f:
        return json.load(f)
