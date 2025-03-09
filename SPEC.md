# Technical Specification

## System Overview
The `prompt-decorators` project is designed to enhance prompt generation through a series of decorators that control various aspects of prompt behavior. The system comprises several core components, including decorators, enums, a registry, exceptions, and utilities. These components work together to provide a flexible and configurable prompt generation framework.

### Main Components
- **Decorators**: Functions that modify the behavior of prompt generation.
- **Enums**: Enumerations used to configure decorators.
- **Registry**: Manages the discovery and usage of decorators.
- **Exceptions**: Custom exceptions for handling errors related to decorators.
- **Utilities**: Helper functions and classes for various tasks.

## Core Functionality
The core functionality of the `prompt-decorators` project revolves around the decorators and their configurations. Each decorator is designed to enforce specific behaviors in prompt generation, controlled by enums and utility functions.

### Primary Features and Their Implementation

#### 1. **Core Decorators and Enums**
- **layered Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/layered.py`
  - **Primary Exported Functions:** `layered`
  - **Importance Score:** 90
  - **Description:** Defines the `layered` decorator, which controls the layering behavior of prompts using enums like `LayeredLevelsEnum` and `LayeredProgressionEnum`.

- **forced_analogy Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/forced_analogy.py`
  - **Primary Exported Functions:** `forced_analogy`
  - **Importance Score:** 85
  - **Description:** Defines the `forced_analogy` decorator, which enforces the generation of analogies in prompts using enums like `ForcedAnalogyComprehensivenessEnum`.

- **deductive Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/deductive.py`
  - **Primary Exported Functions:** `deductive`
  - **Importance Score:** 85
  - **Description:** Defines the `deductive` decorator, which enforces deductive reasoning in prompt generation using enums to control various aspects.

- **decision_matrix Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/decision_matrix.py`
  - **Primary Exported Functions:** `decision_matrix`
  - **Importance Score:** 85
  - **Description:** Defines the `decision_matrix` decorator, which structures prompts using a decision matrix format using enums like `DecisionMatrixScaleEnum`.

- **precision Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/precision.py`
  - **Primary Exported Functions:** `precision`
  - **Importance Score:** 85
  - **Description:** Defines the `precision` decorator, which controls the level of precision in generated prompts using enums like `PrecisionLevelEnum`.

- **step_by_step Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/step_by_step.py`
  - **Primary Exported Functions:** `step_by_step`
  - **Importance Score:** 85
  - **Description:** Defines the `step_by_step` decorator, which structures prompts in a step-by-step format using enums to control the behavior.

- **narrative Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/narrative.py`
  - **Primary Exported Functions:** `narrative`
  - **Importance Score:** 85
  - **Description:** Defines the `narrative` decorator, which structures prompts in a narrative format using enums like `NarrativeLengthEnum` and `NarrativeStructureEnum`.

- **summary Decorator**
  - **File:** `prompt_decorators/decorators/generated/decorators/summary.py`
  - **Primary Exported Functions:** `summary`
  - **Importance Score:** 85
  - **Description:** Defines the `summary` decorator, which generates summary prompts using enums like `SummaryLengthEnum` and `SummaryPositionEnum`.

- **Enums**
  - **File:** `prompt_decorators/decorators/generated/decorators/enums.py`
  - **Primary Exported Functions:** Various enums
  - **Importance Score:** 90
  - **Description:** Defines various enums used across different decorators to control their behavior, including `LayeredLevelsEnum`, `ForcedAnalogyComprehensivenessEnum`, etc.

#### 2. **Core Registry**
- **File:** `prompt_decorators/core/registry.py`
- **Primary Exported Functions:** Registry management functions
- **Importance Score:** 95
- **Description:** Manages the registry of decorators, which is crucial for discovering and using decorators throughout the system.

#### 3. **Core Exceptions**
- **File:** `prompt_decorators/core/exceptions.py`
- **Primary Exported Functions:** Custom exception classes
- **Importance Score:** 80
- **Description:** Defines custom exception classes used across the system to handle errors related to decorators and prompt generation.

#### 4. **Core Utils**
- **File:** `prompt_decorators/utils/__init__.py`
- **Primary Exported Functions:** Various utility classes and functions
- **Importance Score:** 85
- **Description:** Exports various utility classes and functions, including `DecoratorCache`, `DecoratorRegistry`, `DocGenerator`, and others, which are essential for the system's functionality.

#### 5. **Decorator Parser**
- **File:** `prompt_decorators/core/parser.py.bak`
- **Primary Exported Functions:**
  - `DecoratorParser.extract_decorators`
  - `DecoratorParser._create_decorator`
  - `DecoratorParser._parse_parameters`
- **Importance Score:** 90, 85, 80 respectively
- **Description:**
  - `extract_decorators`: Extracts decorator annotations from a given prompt text.
  - `_create_decorator`: Creates an instance of a decorator by name with the given parameters.
  - `_parse_parameters`: Parses a parameter string into a dictionary.

#### 6. **GitHub Workflows**
- **File:** `.github/workflows/code-quality.yml`, `.github/workflows/docs.yml`, `.github/workflows/publish.yml`
- **Primary Exported Functions:**
  - `pre-commit`, `test-matrix`, `type-check`, `docstring-check`, `docs`, `deploy`
- **Importance Score:** 70, 85, 75, 70, 80, 90 respectively
- **Description:**
  - `pre-commit`: Runs pre-commit hooks to ensure code quality.
  - `test-matrix`: Runs tests across multiple Python versions.
  - `type-check`: Performs static type checking on the codebase.
  - `docstring-check`: Checks the docstrings for consistency and correctness.
  - `docs`: Builds and deploys the documentation.
  - `deploy`: Publishes the package to PyPI when a release is created.

#### 7. **Configuration Files**
- **File:** `.pre-commit-config.yaml`, `mkdocs.yml`, `mypy.ini`, `pyproject.toml`, `setup.cfg`
- **Importance Score:** 80, 90, 80, 100, 90 respectively
- **Description:**
  - `.pre-commit-config.yaml`: Configures pre-commit hooks to maintain code quality.
  - `mkdocs.yml`: Configures the MkDocs site for documentation.
  - `mypy.ini`: Configures the MyPy type checker.
  - `pyproject.toml`: Defines the project metadata, dependencies, and tool configurations.
  - `setup.cfg`: Provides additional configuration for the setuptools-based build process.

## Architecture
The `prompt-decorators` project follows a modular architecture where each decorator is a standalone component that can be configured using enums. The registry plays a central role in managing and discovering these decorators. The system is designed to be flexible, allowing for easy addition and configuration of new decorators.

### Data Flow
1. **Input**: Prompt text with decorator annotations.
2. **Processing**:
   - The `DecoratorParser` extracts decorator annotations and parameters from the prompt text.
   - Decorators are instantiated using the registry and their parameters.
   - The decorators modify the prompt text according to their configurations.
3. **Output**: Modified prompt text with the desired behavior enforced by the decorators.
