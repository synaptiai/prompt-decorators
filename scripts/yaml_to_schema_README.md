# YAML to JSON Schema Converter

This directory contains scripts for converting simplified YAML decorator definitions to complete JSON schema files following the registry-entry.schema.json format. The converter uses the Claude 3.7 Sonnet model to intelligently expand the simplified definitions into compliant schema files.

## Scripts

- `yaml_to_schema_converter.py`: The main converter script
- `test_yaml_to_schema.py`: A test script for verifying the converter

## Requirements

- Python 3.9+
- Anthropic API key
- Required Python packages:
  - anthropic
  - pyyaml
  - jsonschema
  - tqdm

## Installation

1. Install the required packages:

```bash
pip install anthropic pyyaml jsonschema tqdm
```

2. Set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --output registry/core
```

### With Custom Options

```bash
python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --output registry/core --batch-size 5 --validate --verbose
```

### Dry Run Mode

```bash
python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --dry-run
```

### Testing

```bash
python scripts/test_yaml_to_schema.py
```

## Command-Line Arguments

- `--input`, `-i`: Path to the input YAML file (required)
- `--output`, `-o`: Directory to save the generated schema files (default: registry/core)
- `--api-key`, `-k`: Anthropic API key (default: from ANTHROPIC_API_KEY environment variable)
- `--schema`, `-s`: Path to the registry-entry.schema.json file (default: schemas/registry-entry.schema.json)
- `--cache-dir`, `-c`: Directory to store cache files (default: .cache/schema_converter)
- `--batch-size`, `-b`: Number of decorators to process in a batch (default: 3)
- `--max-workers`, `-w`: Maximum number of concurrent workers (default: 2)
- `--rate-limit`, `-r`: Delay between API calls to respect rate limits (default: 1.0)
- `--parallel`, `-p`: Process decorators in parallel
- `--force`, `-f`: Overwrite existing files
- `--dry-run`, `-d`: Perform a dry run without saving files
- `--validate`, `-v`: Validate generated schemas
- `--verbose`: Enable verbose logging

## YAML Format

The input YAML file should follow this format:

```yaml
version: 1.0.0
author:
  name: "Author Name"
  email: "author@example.com"
  url: "https://example.com"

decorators:
  - name: DecoratorName
    category: Category
    description: Description of the decorator
    parameters:
      - name: param_name
        type: enum  # enum, string, boolean, number, array
        description: Description of the parameter
        values: [value1, value2, value3]  # Required for enum type
        default: value1  # Optional
        required: false  # Optional
    example: |
      +++DecoratorName(param_name=value2)
      This is an example prompt.
```
Yaml specification available in the schemas directory [simplified-decorator.schema.yaml](/schemas/simplified-decorator.schema.yaml)

## Output Format

The output JSON schema files follow the [registry-entry.schema.json](/schemas/registry-entry.schema.json) format:

```json
{
  "decoratorName": "DecoratorName",
  "version": "1.0.0",
  "description": "Description of the decorator",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://example.com"
  },
  "parameters": [
    {
      "name": "param_name",
      "type": "string",
      "description": "Description of the parameter",
      "enum": ["value1", "value2", "value3"],
      "default": "value1",
      "required": false
    }
  ],
  "transformationTemplate": {
    "instruction": "...",
    "parameterMapping": { ... },
    "placement": "append",
    "compositionBehavior": "accumulate"
  },
  "implementationGuidance": { ... },
  "examples": [ ... ],
  "compatibility": { ... }
}
```

## Features

- **Schema Validation**: Validates generated schemas against the registry-entry.schema.json schema
- **Batch Processing**: Processes decorators in batches to optimize API usage
- **Caching**: Caches API responses to avoid regenerating schemas unnecessarily
- **Smart Error Recovery**: Retries or fixes common issues in API responses
- **Parallel Processing**: Optional concurrent processing with rate limit awareness
- **Dry Run Mode**: Previews what would be generated without making API calls
- **Schema Diff**: Shows differences when regenerating existing schemas
- **Verbose Output Levels**: Configurable logging detail

## Error Handling

The script handles and provides clear messages for:
- YAML parsing errors
- API authentication failures
- Rate limiting issues
- JSON schema validation errors
- File I/O problems
