"""
Advanced examples for the OpenAI prompt decorator demo.

This module contains advanced examples demonstrating the composition of multiple
prompt decorators for more complex use cases.
"""

from typing import Any, Dict, List, Optional

import typer

from ..dynamic_openai_demo import query_with_decorators
from ..utils.logging import log_decorated_prompt, log_info, log_response

app = typer.Typer()


@app.command()
def compound_decorators() -> None:
    """
    Demonstrate combining multiple decorators for a research analysis.
    """
    log_info("Running Compound Decorators example")
    prompt = "Analyze the impact of artificial intelligence on the job market."
    decorators = [
        "StepByStep()",
        "Reasoning(depth='comprehensive')",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def tech_tutorial() -> None:
    """
    Demonstrate creating a technical tutorial with decorators.
    """
    log_info("Running Tech Tutorial example")
    prompt = "Create a tutorial on setting up a Docker container for a Python web application."
    decorators = [
        "StepByStep(numbered=True)",
        "Audience(level='beginner')",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def decision_analysis() -> None:
    """
    Demonstrate decision analysis with a matrix.
    """
    log_info("Running Decision Analysis example")
    prompt = "Compare cloud providers AWS, Azure, and Google Cloud for a medium-sized e-commerce business."
    decorators = [
        "Reasoning(depth='comprehensive')",
        "OutputFormat(format='markdown')",
        "Detailed(depth='comprehensive', examples=true)",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def debate_topic() -> None:
    """
    Demonstrate a balanced debate on a controversial topic.
    """
    log_info("Running Debate Topic example")
    prompt = "Should artificial intelligence development be regulated?"
    decorators = [
        "Reasoning(depth='comprehensive')",
        "StepByStep()",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def layered_explanation() -> None:
    """
    Demonstrate a layered explanation at different depths.
    """
    log_info("Running Layered Explanation example")
    prompt = "Explain how machine learning works."
    # Note: 'layered' is not a valid level for Audience, using 'beginner' instead
    decorators = [
        "Audience(level='beginner')",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def first_principles_analysis() -> None:
    """
    Demonstrate first principles analysis with detailed reasoning.
    """
    log_info("Running First Principles Analysis example")
    prompt = "Analyze the concept of cryptocurrency from first principles."
    decorators = [
        "Reasoning(depth='comprehensive')",
        "StepByStep()",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def critical_review() -> None:
    """
    Demonstrate a critical review using contrarian and steelman approaches.
    """
    log_info("Running Critical Review example")
    prompt = "Evaluate the argument that social media is harmful to society."
    decorators = [
        "NegativeSpace()",
        "Reasoning(depth='comprehensive')",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def creative_problem_solving() -> None:
    """
    Demonstrate creative problem solving with multiple perspectives.
    """
    log_info("Running Creative Problem Solving example")
    prompt = "How can cities better manage waste and recycling?"
    decorators = [
        "Reasoning(depth='moderate')",
        "TreeOfThought(branches=3, depth=3, pruning=false)",
        "Audience(level='expert')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


@app.command()
def strategic_planning() -> None:
    """
    Demonstrate strategic planning with MECE and decision matrix.
    """
    log_info("Running Strategic Planning example")
    prompt = (
        "Develop a digital transformation strategy for a traditional retail business."
    )
    decorators = [
        "StepByStep()",
        "Reasoning(depth='comprehensive')",
        "OutputFormat(format='markdown')",
    ]
    result = query_with_decorators(prompt, decorators)
    # Response is already logged by query_with_decorators


if __name__ == "__main__":
    app()
