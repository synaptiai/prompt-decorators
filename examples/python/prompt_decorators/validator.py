"""Validator for Prompt Decorators implementation."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from jsonschema import Draft7Validator, RefResolver, ValidationError, validators
from pydantic import ValidationError as PydanticValidationError

from .models import (
    APIRequest,
    BaseDecorator,
    OutputFormat,
    ToneStyle,
    ReasoningDecorator,
    StepByStepDecorator,
    OutputFormatDecorator,
    ToneDecorator,
    VersionDecorator,
)


class DecoratorValidator:
    """Validator for Prompt Decorators."""

    def __init__(self, schemas_dir: Union[str, Path]) -> None:
        """Initialize the validator with schema directory.

        Args:
            schemas_dir: Path to the directory containing JSON schemas
        """
        self.schemas_dir = Path(schemas_dir)
        self._load_schemas()
        self._init_validators()

    def _load_schemas(self) -> None:
        """Load all JSON schemas from the schemas directory."""
        self.schemas = {}
        schema_files = [
            "decorator.schema.json",
            "api-request.schema.json",
            "registry-entry.schema.json",
            "extension-package.schema.json",
        ]

        for schema_file in schema_files:
            schema_path = self.schemas_dir / schema_file
            if not schema_path.exists():
                raise FileNotFoundError(f"Schema file not found: {schema_path}")
            
            with open(schema_path, "r") as f:
                self.schemas[schema_file] = json.load(f)

    def _init_validators(self) -> None:
        """Initialize JSON Schema validators with proper reference resolution."""
        self.validators = {}
        
        # Create a resolver that can handle schema references
        schema_store = {}
        for name, schema in self.schemas.items():
            schema_uri = f"file://{self.schemas_dir.resolve()}/{name}"
            schema_store[schema_uri] = schema
            
        for name, schema in self.schemas.items():
            schema_uri = f"file://{self.schemas_dir.resolve()}/{name}"
            resolver = RefResolver(schema_uri, schema, store=schema_store)
            self.validators[name] = Draft7Validator(schema, resolver=resolver)

    def validate_decorator(self, decorator: BaseDecorator) -> List[str]:
        """Validate a single decorator against the decorator schema.

        Args:
            decorator: The decorator instance to validate

        Returns:
            List of validation error messages
        """
        errors = []
        try:
            # Validate using Pydantic model
            decorator_dict = decorator.model_dump()
            
            # Validate against JSON schema
            validator = self.validators["decorator.schema.json"]
            validation_errors = list(validator.iter_errors(decorator_dict))
            
            if validation_errors:
                errors.extend(str(error) for error in validation_errors)
                
        except PydanticValidationError as e:
            errors.extend(str(error) for error in e.errors())
        except Exception as e:
            errors.append(f"Unexpected error: {str(e)}")
            
        return errors

    def validate_api_request(self, request: APIRequest) -> List[str]:
        """Validate an API request against the API request schema.

        Args:
            request: The API request to validate

        Returns:
            List of validation error messages
        """
        errors = []
        try:
            # Validate using Pydantic model
            request_dict = request.model_dump()
            
            # Validate against JSON schema
            validator = self.validators["api-request.schema.json"]
            validation_errors = list(validator.iter_errors(request_dict))
            
            if validation_errors:
                errors.extend(str(error) for error in validation_errors)
                
            # Validate each decorator in the request
            for decorator in request.decorators:
                decorator_errors = self.validate_decorator(decorator)
                if decorator_errors:
                    errors.extend(
                        f"Decorator '{decorator.name}' validation errors: {error}"
                        for error in decorator_errors
                    )
                    
        except PydanticValidationError as e:
            errors.extend(str(error) for error in e.errors())
        except Exception as e:
            errors.append(f"Unexpected error: {str(e)}")
            
        return errors

    def validate_registry_entry(self, entry: Dict[str, Any]) -> List[str]:
        """Validate a registry entry against the registry entry schema.

        Args:
            entry: The registry entry to validate

        Returns:
            List of validation error messages
        """
        errors = []
        try:
            validator = self.validators["registry-entry.schema.json"]
            validation_errors = list(validator.iter_errors(entry))
            errors.extend(str(error) for error in validation_errors)
        except Exception as e:
            errors.append(f"Unexpected error: {str(e)}")
        return errors

    def validate_extension_package(self, package: Dict[str, Any]) -> List[str]:
        """Validate an extension package against the extension package schema.

        Args:
            package: The extension package to validate

        Returns:
            List of validation error messages
        """
        errors = []
        try:
            validator = self.validators["extension-package.schema.json"]
            validation_errors = list(validator.iter_errors(package))
            errors.extend(str(error) for error in validation_errors)
        except Exception as e:
            errors.append(f"Unexpected error: {str(e)}")
        return errors 