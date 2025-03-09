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
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="prompt engineering, llm, ai, decorators, data science",
    python_requires=">=3.11",
)
```

### Step 3: Implementing Decorators

Create a module for each decorator or group of related decorators. Let's implement the `DataAnalysis` decorator first.

Create a file `prompt_decorators_datascience/decorators/analysis.py`:

```python
from prompt_decorators import DecoratorDefinition

data_analysis_decorator = DecoratorDefinition(
    name="DataAnalysis",
    description="Directs LLM to perform exploratory data analysis on provided data",
    category="DataScience",
    parameters=[
        {
            "name": "depth",
            "type": "enum",
            "description": "Depth of analysis",
            "enum": ["basic", "moderate", "comprehensive"],
            "default": "moderate"
        },
        {
            "name": "focus",
            "type": "enum",
            "description": "Primary focus of the analysis",
            "enum": ["patterns", "outliers", "correlations", "distributions", "all"],
            "default": "all"
        },
        {
            "name": "include_visualizations",
            "type": "boolean",
            "description": "Whether to include visualization recommendations",
            "default": True
        }
    ],
    transform_function="""
    let instruction = "Please perform exploratory data analysis on the following data. ";

    // Add depth-specific instructions
    if (depth === "basic") {
        instruction += "Focus on the most important high-level insights and summary statistics. ";
    } else if (depth === "moderate") {
        instruction += "Provide a balanced analysis with key statistics, trends, and notable patterns. ";
    } else if (depth === "comprehensive") {
        instruction += "Conduct a thorough analysis exploring all aspects of the data including distributions, " +
            "relationships, patterns, outliers, and potential issues. ";
    }

    // Add focus-specific instructions
    if (focus === "patterns") {
        instruction += "Focus primarily on identifying patterns and trends in the data. ";
    } else if (focus === "outliers") {
        instruction += "Pay special attention to outliers and anomalies in the data. ";
    } else if (focus === "correlations") {
        instruction += "Emphasize relationships and correlations between variables. ";
    } else if (focus === "distributions") {
        instruction += "Focus on the distributions of variables and their statistical properties. ";
    } else {
        instruction += "Cover all aspects including patterns, outliers, correlations, and distributions. ";
    }

    // Add visualization instructions
    if (include_visualizations) {
        instruction += "For each insight, recommend appropriate visualizations (with code examples if applicable). ";
    }

    // Add structure instructions
    instruction += "Structure your analysis as follows:\\n" +
        "1. Data Overview: Summarize the dataset structure\\n" +
        "2. Summary Statistics: Provide key statistical measures\\n" +
        "3. Key Insights: Highlight the most important findings";

    if (focus !== "all") {
        instruction += "\\n4. Detailed Analysis: " + focus.charAt(0).toUpperCase() + focus.slice(1);
    } else {
        instruction += "\\n4. Detailed Analysis: Patterns, outliers, correlations, and distributions";
    }

    if (include_visualizations) {
        instruction += "\\n5. Visualization Recommendations: Suggest appropriate charts with explanations";
    }

    instruction += "\\n6. Next Steps: Suggest further analyses or actions based on the findings";

    instruction += "\\n\\nHere's the data to analyze:\\n\\n";

    return instruction + text;
    """
)
```

Now create the `DataVisualization` decorator in `prompt_decorators_datascience/decorators/visualization.py`:

```python
from prompt_decorators import DecoratorDefinition

data_visualization_decorator = DecoratorDefinition(
    name="DataVisualization",
    description="Directs LLM to provide visualization recommendations and code for data",
    category="DataScience",
    parameters=[
        {
            "name": "library",
            "type": "enum",
            "description": "Visualization library to use",
            "enum": ["matplotlib", "seaborn", "plotly", "altair", "any"],
            "default": "any"
        },
        {
            "name": "chart_types",
            "type": "string",
            "description": "Comma-separated list of chart types to include",
            "default": "all"
        },
        {
            "name": "include_code",
            "type": "boolean",
            "description": "Whether to include code examples",
            "default": True
        }
    ],
    transform_function="""
    let instruction = "Please recommend visualizations for the following data. ";

    // Add library-specific instructions
    if (library !== "any") {
        instruction += `Use the ${library} library for all visualizations. `;
    } else {
        instruction += "Use the most appropriate visualization library for each chart type. ";
    }

    // Add chart type instructions
    if (chart_types !== "all") {
        const chartList = chart_types.split(",").map(t => t.trim());
        instruction += `Focus on the following chart types: ${chartList.join(", ")}. `;
    } else {
        instruction += "Recommend a diverse set of chart types appropriate for the data. ";
    }

    // Add code instructions
    if (include_code) {
        instruction += "For each visualization, provide Python code that would create the chart. Ensure the code is correct, complete, and ready to run. ";
    } else {
        instruction += "Describe each visualization clearly but do not include code examples. ";
    }

    // Add structure instructions
    instruction += "Structure your response as follows:\\n" +
        "1. Data Overview: Brief summary of the data\\n" +
        "2. Visualization Recommendations: For each visualization include:\\n" +
        "   a. Purpose: What insight this visualization will provide\\n" +
        "   b. Chart Type: The specific type of chart recommended\\n" +
        "   c. Variables: Which data variables should be included";

    if (include_code) {
        instruction += "\\n   d. Code: Python code to generate this visualization";
    }

    instruction += "\\n3. Dashboard Suggestion: How these visualizations could be combined into a dashboard\\n";

    instruction += "\\nHere's the data to visualize:\\n\\n";

    return instruction + text;
    """
)
```

Repeat this process for the other decorators in your extension.

### Step 4: Registering Decorators

In your package's `__init__.py`, import and register all your decorators:

```python
"""
Prompt Decorators - Data Science Extension

A collection of prompt decorators for data science workflows.
"""

from prompt_decorators import register_decorator

# Import decorators
from .decorators.analysis import data_analysis_decorator
from .decorators.visualization import data_visualization_decorator
# Import other decorators...

# Register all decorators
def register_all_decorators():
    """Register all decorators from this extension."""
    register_decorator(data_analysis_decorator)
    register_decorator(data_visualization_decorator)
    # Register other decorators...

# Auto-register when the package is imported
register_all_decorators()

# Export public API
__all__ = [
    "data_analysis_decorator",
    "data_visualization_decorator",
    # Add other decorators...
]
```

In your decorators' `__init__.py`, export the decorators:

```python
"""Data science decorators."""

from .analysis import data_analysis_decorator
from .visualization import data_visualization_decorator
# Import other decorators...

__all__ = [
    "data_analysis_decorator",
    "data_visualization_decorator",
    # Add other decorators...
]
```

### Step 5: Creating Composite Decorators

You can also create composite decorators that combine multiple data science decorators for common workflows:

```python
from prompt_decorators import DecoratorDefinition

data_science_workflow_decorator = DecoratorDefinition(
    name="DataScienceWorkflow",
    description="Comprehensive data science workflow combining analysis, visualization, and insights",
    category="DataScience",
    parameters=[
        {
            "name": "workflow_stage",
            "type": "enum",
            "description": "Stage of the data science workflow",
            "enum": ["exploration", "preprocessing", "modeling", "evaluation", "full"],
            "default": "full"
        },
        {
            "name": "detail_level",
            "type": "enum",
            "description": "Level of detail in the response",
            "enum": ["brief", "standard", "detailed"],
            "default": "standard"
        }
    ],
    transform_function="""
    // Import our component decorators from this extension
    const dataAnalysis = createDecoratorInstance('DataAnalysis', {
        depth: detail_level === "brief" ? "basic" : detail_level === "detailed" ? "comprehensive" : "moderate",
        include_visualizations: true
    });

    const dataViz = createDecoratorInstance('DataVisualization', {
        include_code: true
    });

    // Add standard decorators
    const outputFormat = createDecoratorInstance('OutputFormat', { format: 'markdown' });
    const reasoning = createDecoratorInstance('Reasoning', {
        depth: detail_level === "brief" ? "basic" : detail_level === "detailed" ? "comprehensive" : "moderate"
    });

    let result = text;

    // Apply different decorators based on workflow stage
    if (workflow_stage === "exploration" || workflow_stage === "full") {
        result = dataAnalysis(result);
    }

    if (workflow_stage === "preprocessing") {
        // Use a hypothetical DataCleaning decorator
        const dataCleaning = createDecoratorInstance('DataCleaning');
        result = dataCleaning(result);
    }

    if ((workflow_stage === "exploration" || workflow_stage === "full") && detail_level !== "brief") {
        result = dataViz(result);
    }

    if (workflow_stage === "modeling" || workflow_stage === "full") {
        // Use a hypothetical ModelSelection decorator
        const modelSelection = createDecoratorInstance('ModelSelection');
        result = modelSelection(result);
    }

    if (workflow_stage === "evaluation" || workflow_stage === "full") {
        // Use a hypothetical ModelEvaluation decorator
        const modelEvaluation = createDecoratorInstance('ModelEvaluation');
        result = modelEvaluation(result);
    }

    // Always apply these decorators
    result = reasoning(result);
    result = outputFormat(result);

    return result;
    """
)
```

Add this to your extension and register it along with the other decorators.

### Step 6: Testing Your Extension

Create a test script to ensure your decorators work as expected:

```python
# test_extension.py
import openai
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance
# Import your extension
import prompt_decorators_datascience

# Sample data
sample_data = """
Age,Income,Education,Job_Experience,Credit_Score
32,65000,Bachelors,8,720
45,85000,Masters,15,780
23,35000,High School,2,650
37,72000,Bachelors,12,710
51,95000,PhD,20,800
29,48000,Associates,5,680
"""

# Test DataAnalysis decorator
def test_data_analysis():
    # Using inline syntax
    prompt = f"""
    +++DataAnalysis(depth=comprehensive, focus=correlations)
    {sample_data}
    """

    transformed_prompt = apply_dynamic_decorators(prompt)
    print("Data Analysis Transformed Prompt:")
    print("-" * 80)
    print(transformed_prompt)
    print("-" * 80)

    # Using programmatic approach
    data_analysis = create_decorator_instance("DataAnalysis", depth="comprehensive", focus="correlations")
    transformed_prompt_2 = data_analysis(sample_data)

    # They should be identical
    assert transformed_prompt == transformed_prompt_2

# Test DataVisualization decorator
def test_data_visualization():
    # Using inline syntax
    prompt = f"""
    +++DataVisualization(library=seaborn, include_code=true)
    {sample_data}
    """

    transformed_prompt = apply_dynamic_decorators(prompt)
    print("Data Visualization Transformed Prompt:")
    print("-" * 80)
    print(transformed_prompt)
    print("-" * 80)

# Test with an LLM
def test_with_llm():
    # Using DataAnalysis decorator
    prompt = f"""
    +++DataAnalysis(depth=moderate, focus=all)
    {sample_data}
    """

    transformed_prompt = apply_dynamic_decorators(prompt)

    # Replace with your API key
    openai.api_key = "your-api-key-here"

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": transformed_prompt}],
        temperature=0.7
    )

    print("LLM Response:")
    print("-" * 80)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    test_data_analysis()
    test_data_visualization()
    # Uncomment to test with an actual LLM
    # test_with_llm()
```

### Step 7: Documenting Your Extension

Create thorough documentation for your extension. At minimum, include:

1. **README.md**: Overview, installation, and basic usage
2. **API Documentation**: Details of each decorator
3. **Examples**: Practical examples of using each decorator
4. **Integration Guide**: How to integrate with existing workflows

Here's a sample README.md:

```markdown
# Prompt Decorators - Data Science Extension

A collection of specialized prompt decorators for data science workflows. This extension for the [Prompt Decorators](https://github.com/synaptiai/prompt-decorators) framework provides decorators for data analysis, visualization, model evaluation, and more.

## Installation

```bash
pip install prompt-decorators-datascience
```

## Usage

```python
from prompt_decorators import apply_dynamic_decorators
import prompt_decorators_datascience  # This registers all the decorators

# Using inline syntax
prompt = """
+++DataAnalysis(depth=comprehensive, focus=correlations)
Here's my dataset:
Age,Income,Education,Job_Experience,Credit_Score
32,65000,Bachelors,8,720
45,85000,Masters,15,780
23,35000,High School,2,650
...
"""

transformed_prompt = apply_dynamic_decorators(prompt)
# Now send transformed_prompt to your LLM
```

## Available Decorators

### DataAnalysis

Directs LLM to perform exploratory data analysis on provided data.

**Parameters:**
- `depth` (enum): Depth of analysis (basic, moderate, comprehensive)
- `focus` (enum): Primary focus (patterns, outliers, correlations, distributions, all)
- `include_visualizations` (boolean): Whether to include visualization recommendations

### DataVisualization

Directs LLM to provide visualization recommendations and code for data.

**Parameters:**
- `library` (enum): Visualization library to use (matplotlib, seaborn, plotly, altair, any)
- `chart_types` (string): Comma-separated list of chart types to include
- `include_code` (boolean): Whether to include code examples

### DataScienceWorkflow

Comprehensive data science workflow combining analysis, visualization, and insights.

**Parameters:**
- `workflow_stage` (enum): Stage of the data science workflow (exploration, preprocessing, modeling, evaluation, full)
- `detail_level` (enum): Level of detail in the response (brief, standard, detailed)

## License

MIT
```

### Step 8: Packaging and Distribution

Once your extension is ready for distribution, create a package:

```bash
# Create a source distribution
python setup.py sdist

# Create a wheel package
python setup.py bdist_wheel
```

If you want to publish to PyPI:

```bash
# Install twine
pip install twine

# Upload to PyPI
twine upload dist/*
```

Alternatively, you can publish your package to GitHub and install directly from there:

```bash
pip install git+https://github.com/yourusername/prompt-decorators-datascience.git
```

## Advanced Extension Development

### Configuration Management

For more complex extensions, you might want to add configuration management:

```python
# prompt_decorators_datascience/config.py

class DataScienceExtensionConfig:
    """Configuration for the data science extension."""

    def __init__(self):
        self.default_visualization_library = "matplotlib"
        self.include_code_by_default = True
        self.default_analysis_depth = "moderate"

    def update_from_dict(self, config_dict):
        """Update configuration from a dictionary."""
        for key, value in config_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        """String representation of the configuration."""
        return str(vars(self))

# Default configuration
config = DataScienceExtensionConfig()

def configure(config_dict):
    """Configure the extension with custom settings."""
    config.update_from_dict(config_dict)
```

Then use this configuration in your decorators:

```python
from .config import config

# In your transform_function:
"""
// Use configuration
const default_library = "${config.default_visualization_library}";
// ...
"""
```

### Versioning Strategy

Implement proper versioning:

```python
# prompt_decorators_datascience/__init__.py

__version__ = "0.1.0"
```

Follow semantic versioning:
- Increment MAJOR version for incompatible API changes
- Increment MINOR version for backwards-compatible new features
- Increment PATCH version for backwards-compatible bug fixes

### Testing Framework

For comprehensive testing, use pytest:

```python
# tests/test_decorators.py
import pytest
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance
import prompt_decorators_datascience

def test_data_analysis_decorator():
    # Create a test prompt
    test_data = "Age,Income\n30,50000\n40,70000"
    decorator = create_decorator_instance("DataAnalysis", depth="basic")

    # Apply the decorator
    result = decorator(test_data)

    # Assertions
    assert "Please perform exploratory data analysis" in result
    assert "Focus on the most important high-level insights" in result
    assert test_data in result

# Add more tests for other decorators...
```

Create a tox.ini file for multi-environment testing:

```ini
[tox]
envlist = py38, py39, py310

[testenv]
deps =
    pytest
    prompt-decorators
commands =
    pytest
```

## Best Practices for Extension Development

1. **Focus on a Domain**: Keep your extension focused on a specific domain or use case
2. **Maintain Compatibility**: Ensure your decorators work well with core decorators
3. **Provide Sensible Defaults**: Make your decorators usable without extensive configuration
4. **Version Dependencies**: Specify compatible versions of prompt-decorators
5. **Document Extensively**: Create thorough documentation with examples
6. **Test Thoroughly**: Test with different LLMs to ensure compatibility
7. **Manage Conflicts**: Document any conflicts with core decorators
8. **Provide Examples**: Include real-world examples of using your decorators

## Extension Ideas

Here are some ideas for decorator extensions:

1. **Legal Decorators**: For legal document analysis, contract generation, and case research
2. **Medical Decorators**: For clinical notes, medical literature, and diagnosis assistance
3. **Creative Writing**: For storytelling, character development, and narrative structure
4. **Academic Writing**: For research papers, literature reviews, and academic formatting
5. **Software Development**: For code generation, documentation, and technical specifications
6. **Marketing**: For content creation, ad copy, and marketing analysis
7. **Financial Analysis**: For investment analysis, financial reporting, and risk assessment

## Next Steps

After creating your extension:

1. Share it with the community
2. Gather feedback and iterate on your design
3. Add more specialized decorators
4. Create tutorials and examples
5. Integrate with other tools and frameworks

By developing extensions, you contribute to the Prompt Decorators ecosystem and help establish best practices for prompt engineering in your domain.
