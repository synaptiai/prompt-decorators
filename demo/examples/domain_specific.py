"""
Domain-specific examples for the OpenAI prompt decorator demo.

This module contains examples of using prompt decorators for specific domains
such as data science, education, creative writing, and more.
"""

from typing import Any, Dict, List, Optional

import typer

from ..dynamic_openai_demo import query_with_decorators
from ..utils.logging import log_decorated_prompt, log_info, log_response

app = typer.Typer()


@app.command()
def data_science() -> None:
    """
    Demonstrate prompt decorators for data analysis tasks.
    """
    log_info("Running Data Science example")
    prompt = "Explain how to approach a time series forecasting problem for retail sales data."
    decorators = [
        "StepByStep()",
        "Reasoning(depth='comprehensive')",
        "Audience(level='intermediate')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def educational_content() -> None:
    """
    Demonstrate prompt decorators for educational content.
    """
    log_info("Running Educational Content example")
    prompt = "Create a lesson plan for teaching the concept of photosynthesis to middle school students."
    decorators = [
        "StepByStep()",
        "Audience(level='beginner')",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def creative_writing() -> None:
    """
    Demonstrate prompt decorators for creative writing.
    """
    log_info("Running Creative Writing example")
    prompt = "Write a short story about a character who discovers an unusual ability."
    decorators = [
        "Tone(style='casual')",
        "Detailed(depth='comprehensive', examples=true)",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def product_management() -> None:
    """
    Demonstrate prompt decorators for product management tasks.
    """
    log_info("Running Product Management example")
    prompt = "Create a product requirements document for a mobile health tracking app."
    decorators = [
        "StepByStep()",
        "Detailed(depth='comprehensive', examples=true)",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def scientific_review() -> None:
    """
    Demonstrate prompt decorators for scientific literature review.
    """
    log_info("Running Scientific Review example")
    prompt = "Summarize the current understanding of climate change impacts on ocean ecosystems."
    decorators = [
        "Reasoning(depth='comprehensive')",
        "Audience(level='expert')",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def technical_documentation() -> None:
    """
    Demonstrate prompt decorators for creating technical documentation.
    """
    log_info("Running Technical Documentation example")
    prompt = (
        "Create API documentation for a REST service that manages user authentication."
    )
    decorators = [
        "StepByStep()",
        "Audience(level='technical')",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def business_strategy() -> None:
    """
    Demonstrate prompt decorators for business strategy analysis.
    """
    log_info("Running Business Strategy example")
    prompt = "Analyze the competitive landscape of the electric vehicle market."
    decorators = [
        "Reasoning(depth='comprehensive')",
        "StepByStep()",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def legal_analysis() -> None:
    """
    Demonstrate prompt decorators for legal document analysis.
    """
    log_info("Running Legal Analysis example")
    prompt = "Analyze the key components of a standard non-disclosure agreement."
    decorators = [
        "StepByStep()",
        "Tone(style='formal')",
        "Detailed(depth='comprehensive', examples=true)",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def medical_explanation() -> None:
    """
    Demonstrate prompt decorators for medical content.
    """
    log_info("Running Medical Explanation example")
    prompt = "Explain how vaccines work and their importance in public health."
    decorators = [
        "Audience(level='beginner')",
        "StepByStep()",
        "OutputFormat(format='markdown')",
    ]

    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


if __name__ == "__main__":
    app()
