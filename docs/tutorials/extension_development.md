# Tutorial: Extension Development

This tutorial will guide you through the process of developing extensions for the Prompt Decorators framework, specifically focusing on creating packages of domain-specific decorators. By the end, you'll know how to design, implement, and distribute your own decorator packages.

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators package (`pip install prompt-decorators`)
2. Completed the [Creating Custom Decorators](creating_custom_decorator.md) tutorial
3. Completed the [Combining Decorators](combining_decorators.md) tutorial
4. Basic understanding of Python package development

## What are Decorator Extensions?

Decorator extensions are collections of related decorators packaged together for a specific domain or purpose. They extend the functionality of the core framework by providing specialized decorators for particular use cases. Examples include:

- **Data Science**: Decorators for data analysis, visualization, and machine learning tasks
- **Medical**: Decorators for clinical reports, medical terminology, and research
- **Legal**: Decorators for legal document drafting, case analysis, and contract review
- **Education**: Decorators for lesson planning, educational content, and assessments

## Why Create Extensions?

Creating decorator extensions offers several benefits:

- **Reusability**: Package common decorators for easy reuse
- **Domain Specialization**: Create decorators tailored to specific fields
- **Distribution**: Share your decorators with the community
- **Standardization**: Establish consistent prompt engineering practices
- **Compatibility**: Ensure decorators work well together

## Extension Development Workflow

The general workflow for developing a decorator extension is:

1. **Plan**: Define the scope and purpose of your extension
2. **Design**: Design the individual decorators and their interactions
3. **Implement**: Create and test the decorators
4. **Package**: Structure your code as a Python package
5. **Document**: Create comprehensive documentation
6. **Distribute**: Publish your extension

Let's walk through each step with a concrete example.

## Example: Developing a Data Science Extension

For this tutorial, we'll create a "Data Science Decorator Extension" that includes specialized decorators for data analysis tasks.

### Step 1: Planning Your Extension

First, define the scope and purpose:

- **Name**: `prompt-decorators-datascience`
- **Purpose**: Enhance LLM prompts for data science workflows
- **Target Users**: Data scientists, analysts, and ML engineers
- **Core Functionality**: Data analysis, visualization, model training, and interpretation

Next, outline the decorators you want to include:

1. `DataAnalysis`: For exploratory data analysis
2. `DataVisualization`: For creating visualization specifications
3. `ModelEvaluation`: For evaluating ML model performance
4. `StatisticalSummary`: For statistical analysis of data
5. `DataCleaning`: For data preprocessing suggestions

### Step 2: Setting Up Your Project

Create a project directory structure:

```bash
mkdir prompt-decorators-datascience
cd prompt-decorators-datascience

# Create basic package structure
mkdir -p prompt_decorators_datascience/decorators
touch prompt_decorators_datascience/__init__.py
touch prompt_decorators_datascience/decorators/__init__.py
touch setup.py
touch README.md
touch LICENSE
```

Set up your `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="prompt-decorators-datascience",
    version="0.1.0",
    description="Data Science decorators for the Prompt Decorators framework",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "prompt-decorators>=0.3.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.11",
)
```

Create a basic README.md:

```markdown
    # Prompt Decorators: Data Science Extension

    This package extends the [Prompt Decorators](https://github.com/synaptiai/prompt-decorators) framework with decorators specifically designed for data science workflows.

    ## Installation

    ```bash
    pip install prompt-decorators-datascience
    ```

    ## Features

    - Data analysis decorators
    - Visualization specification decorators
    - Model evaluation decorators
    - Statistical summary decorators
    - Data cleaning decorators

    ## Usage

    ```python
    from prompt_decorators import apply_dynamic_decorators
    from prompt_decorators_datascience import register_datascience_decorators

    # Register the data science decorators
    register_datascience_decorators()

    # Use the decorators in your prompts
    prompt = """
    +++DataAnalysis(depth="exploratory", focus="correlations")
    Please analyze this dataset:

    [dataset content...]
    """

    transformed_prompt = apply_dynamic_decorators(prompt)
    ```

    ## Documentation

    For full documentation, visit [documentation link].
```

### Step 3: Implementing Your Decorators

Now, let's implement the decorators for our extension. We'll start with the `DataAnalysis` decorator:

```python
# prompt_decorators_datascience/decorators/data_analysis.py

from prompt_decorators import DecoratorDefinition, register_decorator

def data_analysis_transform(text, focus="general", visualize=True, statistical=True):
    """
    Transform function for the DataAnalysis decorator.

    Args:
        text (str): The original prompt text
        focus (str): The focus area of the analysis
        visualize (bool): Whether to include visualization suggestions
        statistical (bool): Whether to include statistical analysis

    Returns:
        str: The transformed prompt text
    """
    instruction = "Perform exploratory data analysis on the following data. "

    # Add focus-specific instructions
    if focus == "outliers":
        instruction += "Focus on identifying and analyzing outliers in the data. "
    elif focus == "patterns":
        instruction += "Focus on identifying patterns, trends, and relationships in the data. "
    elif focus == "distributions":
        instruction += "Focus on analyzing the distributions of variables in the data. "
    else:
        instruction += "Provide a general exploratory analysis of the data. "

    # Add visualization instructions
    if visualize:
        instruction += "Include suggestions for appropriate visualizations to illustrate key findings. "

    # Add statistical instructions
    if statistical:
        instruction += "Include relevant statistical measures and tests to support your analysis. "

    # Add structure instructions
    instruction += "Structure your analysis as follows:\n" \
                 "1. Data overview\n" \
                 "2. Key variables and their characteristics\n" \
                 "3. Relationships between variables\n" \
                 "4. Notable patterns or anomalies\n" \
                 "5. Recommendations for further analysis\n\n"

    # Return the transformed text
    return instruction + text

# Create the decorator definition
data_analysis_decorator = DecoratorDefinition(
    name="DataAnalysis",
    description="Transforms a prompt into instructions for exploratory data analysis",
    category="DataScience",
    parameters=[
        {
            "name": "focus",
            "type": "enum",
            "description": "The focus area of the analysis",
            "enum_values": ["general", "outliers", "patterns", "distributions"],
            "default": "general"
        },
        {
            "name": "visualize",
            "type": "boolean",
            "description": "Whether to include visualization suggestions",
            "default": True
        },
        {
            "name": "statistical",
            "type": "boolean",
            "description": "Whether to include statistical analysis",
            "default": True
        }
    ],
    transform_function=data_analysis_transform
)

# Export the decorator
def register_decorators():
    """Register all decorators in this module."""
    register_decorator(data_analysis_decorator)
```

### Step 4: Implementing Individual Decorators

Let's implement one of the decorators as an example:

```python
# prompt_decorators_datascience/decorators/data_analysis.py
"""Data analysis decorator implementation."""

from prompt_decorators import DecoratorDefinition

def data_analysis_transform(text, depth="exploratory", focus="all", visualize=True, summary=True):
    """
    Transform function for the DataAnalysis decorator.

    Args:
        text (str): The input text containing the data to analyze
        depth (str): How deep the analysis should be
        focus (str): What aspects of the data to focus on
        visualize (bool): Whether to suggest visualizations
        summary (bool): Whether to include a summary

    Returns:
        str: The transformed prompt with data analysis instructions
    """
    instruction = "Please perform a data analysis on the provided dataset. "

    # Add depth-specific instructions
    if depth == "exploratory":
        instruction += "Conduct an exploratory data analysis to understand the basic properties of the data. "
    elif depth == "descriptive":
        instruction += "Provide a descriptive analysis with summary statistics and distributions. "
    elif depth == "inferential":
        instruction += "Perform an inferential analysis to test hypotheses and make predictions. "
    elif depth == "comprehensive":
        instruction += "Conduct a comprehensive analysis covering exploratory, descriptive, and inferential statistics. "

    # Add focus-specific instructions
    if focus == "correlations":
        instruction += "Focus on identifying correlations between variables. "
    elif focus == "outliers":
        instruction += "Pay special attention to outliers and anomalies in the data. "
    elif focus == "trends":
        instruction += "Emphasize temporal trends and patterns in the data. "
    elif focus != "all":
        instruction += f"Focus particularly on {focus} in your analysis. "

    # Add visualization instructions
    if visualize:
        instruction += ("Include recommendations for appropriate data visualizations "
                        "that would help understand the data better. ")

    # Add summary instructions
    if summary:
        instruction += ("Provide a clear summary of your findings at the beginning "
                        "of your response. ")

    # Structure the response
    instruction += """
Structure your analysis as follows:
1. Summary of Findings
2. Data Overview (dimensions, types, missing values)
3. Descriptive Statistics
4. Key Insights
5. Recommendations for Further Analysis
"""

    # Combine with the original prompt
    return instruction + "\n\n" + text

# Create the decorator definition
data_analysis_decorator = DecoratorDefinition(
    name="DataAnalysis",
    description="Transforms a prompt into instructions for analyzing data",
    category="Data Science",
    parameters=[
        {
            "name": "depth",
            "type": "enum",
            "description": "How deep the analysis should be",
            "enum": ["exploratory", "descriptive", "inferential", "comprehensive"],
            "default": "exploratory"
        },
        {
            "name": "focus",
            "type": "string",
            "description": "What aspects of the data to focus on",
            "default": "all"
        },
        {
            "name": "visualize",
            "type": "boolean",
            "description": "Whether to suggest visualizations",
            "default": True
        },
        {
            "name": "summary",
            "type": "boolean",
            "description": "Whether to include a summary",
            "default": True
        }
    ],
    transform_function=data_analysis_transform
)
```

Similarly, implement the other decorators in their respective files.

### Step 5: Creating Tests

Create a tests directory and add tests for your decorators:

```python
# tests/test_data_analysis.py
import unittest
from prompt_decorators import apply_dynamic_decorators, register_decorator
from prompt_decorators_datascience.decorators.data_analysis import data_analysis_decorator

class TestDataAnalysisDecorator(unittest.TestCase):

    def setUp(self):
        # Register the decorator for testing
        register_decorator(data_analysis_decorator)

    def test_basic_transformation(self):
        prompt = """
+++DataAnalysis(depth="exploratory", focus="correlations")
Analyze this dataset:
ID, Age, Income, Education
1, 25, 50000, Bachelor's
2, 40, 75000, Master's
3, 30, 60000, Bachelor's
"""
        transformed = apply_dynamic_decorators(prompt)

        # Check that the transformation includes expected elements
        self.assertIn("exploratory data analysis", transformed)
        self.assertIn("identifying correlations", transformed)
        self.assertIn("Structure your analysis", transformed)
        self.assertIn("Analyze this dataset:", transformed)

    def test_different_parameters(self):
        prompt = """
+++DataAnalysis(depth="comprehensive", focus="outliers", visualize=false)
Analyze this dataset:
[data here]
"""
        transformed = apply_dynamic_decorators(prompt)

        # Check parameter-specific instructions
        self.assertIn("comprehensive analysis", transformed)
        self.assertIn("outliers and anomalies", transformed)
        self.assertNotIn("recommendations for appropriate data visualizations", transformed)

if __name__ == "__main__":
    unittest.main()
```

### Step 6: Documentation

Create detailed documentation for your extension. For example, create a `docs` directory with specific documentation for each decorator:

```markdown
    # DataAnalysis Decorator

    The `DataAnalysis` decorator transforms a prompt into instructions for analyzing data. It guides the LLM to perform various types of data analysis depending on the parameters.

    ## Parameters

    - **depth** (enum): How deep the analysis should be
    - `exploratory`: Basic exploration of the data properties
    - `descriptive`: Summary statistics and distributions
    - `inferential`: Hypothesis testing and predictions
    - `comprehensive`: Complete analysis covering all aspects
    - Default: `exploratory`

    - **focus** (string): What aspects of the data to focus on
    - Examples: `correlations`, `outliers`, `trends`, `distributions`, or any custom focus
    - Default: `all`

    - **visualize** (boolean): Whether to suggest visualizations
    - Default: `true`

    - **summary** (boolean): Whether to include a summary
    - Default: `true`

    ## Examples

    ### Basic Usage

    ```python
    from prompt_decorators import apply_dynamic_decorators
    from prompt_decorators_datascience import register_datascience_decorators

    # Register the decorators
    register_datascience_decorators()

    prompt = """
    +++DataAnalysis(depth="exploratory", focus="correlations")
    Analyze this dataset:

    User ID, Age, Purchase Amount, Frequency
    1, 25, 120.50, 3
    2, 34, 75.20, 5
    3, 19, 30.00, 1
    4, 45, 200.75, 8
    """

    transformed_prompt = apply_dynamic_decorators(prompt)
    ```

    ### Comprehensive Analysis

    ```python
    prompt = """
    +++DataAnalysis(depth="comprehensive", focus="customer segments", visualize=true)
    Please analyze this customer data and identify key patterns:

    [dataset content...]
    """
    ```
```

### Step 7: Publishing Your Extension

Once you've implemented and tested your extension, you can publish it to PyPI:

```bash
# Install build tools
pip install build twine

# Build the distribution
python -m build

# Upload to PyPI
twine upload dist/*
```

## Alternative: Class-Based Implementation

If you prefer a class-based approach for more complex decorators, you can use the `DecoratorBase` class:

```python
# prompt_decorators_datascience/decorators/model_evaluation.py

from prompt_decorators import DecoratorBase, register_decorator

class ModelEvaluationDecorator(DecoratorBase):
    """Class-based decorator for ML model evaluation."""

    def __init__(self, model_type="classifier", metrics=None, error_analysis=True):
        """
        Initialize the ModelEvaluation decorator.

        Args:
            model_type (str): Type of model to evaluate
            metrics (list): List of metrics to include
            error_analysis (bool): Whether to include error analysis
        """
        super().__init__()  # Initialize the base class
        self.model_type = model_type
        self.metrics = metrics or self._default_metrics()
        self.error_analysis = error_analysis

    def _default_metrics(self):
        """Get default metrics based on model type."""
        if self.model_type == "classifier":
            return ["accuracy", "precision", "recall", "f1"]
        elif self.model_type == "regressor":
            return ["rmse", "mae", "r2"]
        elif self.model_type == "cluster":
            return ["silhouette", "inertia", "davies_bouldin"]
        else:
            return ["custom"]

    def transform(self, text):
        """Transform the input text to focus on model evaluation."""
        instruction = f"Evaluate the {self.model_type} model based on the following data. "

        # Add metrics instructions
        instruction += f"Include the following evaluation metrics: {', '.join(self.metrics)}. "

        # Add error analysis instructions
        if self.error_analysis:
            instruction += "Perform error analysis to identify patterns in misclassifications or prediction errors. "

        # Add structure instructions
        instruction += "Structure your evaluation as follows:\n" \
                    "1. Model performance summary\n" \
                    "2. Detailed metrics analysis\n" \
                    "3. Strengths and weaknesses\n" \
                    "4. Recommendations for improvement\n\n"

        return instruction + text

# Register the class-based decorator
def register_class_decorators():
    """Register all class-based decorators."""
    register_decorator(ModelEvaluationDecorator,
                      name="ModelEvaluation",
                      description="Decorator for ML model evaluation",
                      category="DataScience")
```

## Creating a Decorator Registry

For more advanced extensions, you might want to create a registry file that defines all your decorators in a structured format using the defined [registry decorator schema](/schemas/registry-entry.schema.json):

```python
# prompt_decorators_datascience/registry.py
"""Registry of all data science decorators."""

DATASCIENCE_DECORATORS = [
    {
        "name": "DataAnalysis",
        "description": "Transforms a prompt into instructions for analyzing data",
        "category": "Data Science",
        "parameters": [
            {
                "name": "depth",
                "type": "enum",
                "description": "How deep the analysis should be",
                "enum": ["exploratory", "descriptive", "inferential", "comprehensive"],
                "default": "exploratory"
            },
            # Other parameters...
        ],
        "transform_module": "prompt_decorators_datascience.decorators.data_analysis",
        "transform_function": "data_analysis_transform"
    },
    # Other decorator definitions...
]

def load_from_registry():
    """
    Load all decorators from the registry and return decorator definitions.

    This allows for more dynamic loading of decorators.
    """
    from prompt_decorators import DecoratorDefinition
    import importlib

    decorator_definitions = []

    for decorator_info in DATASCIENCE_DECORATORS:
        # Dynamically import the transform function
        module = importlib.import_module(decorator_info["transform_module"])
        transform_function = getattr(module, decorator_info["transform_function"])

        # Create the decorator definition
        decorator_def = DecoratorDefinition(
            name=decorator_info["name"],
            description=decorator_info["description"],
            category=decorator_info["category"],
            parameters=decorator_info["parameters"],
            transform_function=transform_function
        )

        decorator_definitions.append(decorator_def)

    return decorator_definitions
```

## Conclusion

In this tutorial, you've learned how to:

1. Plan and design a decorator extension
2. Set up a Python package for your extension
3. Implement decorator functionality
4. Create tests for your decorators
5. Document your extension
6. Prepare for publishing to PyPI

By following these steps, you can create specialized decorator extensions that enhance the Prompt Decorators framework for specific domains or use cases. This allows you to build reusable libraries of prompt engineering patterns that can be shared with others in your field.

## Next Steps

- Implement a full set of decorators for your domain
- Create examples demonstrating your decorators in real-world scenarios
- Explore integrations with domain-specific libraries and frameworks
- Contribute your extension to the community
- Consider creating a web interface for your decorators
