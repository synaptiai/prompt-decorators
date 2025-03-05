"""
Basic examples for the OpenAI prompt decorator demo.

This module contains examples demonstrating individual prompt decorators
with simple use cases.
"""

from typing import Any, Dict, List, Optional

import typer

from ..openai_demo import query_with_decorators
from ..utils.logging import log_decorated_prompt, log_info, log_response

app = typer.Typer()


@app.command()
def reasoning(depth: str = "comprehensive") -> None:
    """Demonstrate the Reasoning decorator"""
    log_info(f"Running Reasoning example with depth={depth}")
    prompt = "Explain the concept of recursion in programming."
    # Ensure depth is one of: 'basic', 'moderate', or 'comprehensive'
    decorator = f"Reasoning(depth='{depth}')"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def step_by_step(numbered: bool = True) -> None:
    """Demonstrate the StepByStep decorator"""
    log_info(f"Running StepByStep example with numbered={numbered}")
    prompt = "Explain how to implement binary search."
    decorator = f"StepByStep(numbered={numbered})"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def output_format(format: str = "markdown") -> None:
    """Demonstrate the OutputFormat decorator"""
    log_info(f"Running OutputFormat example with format={format}")
    prompt = "List the top 3 programming languages and their key features."
    # Ensure format is one of: 'json', 'markdown', 'yaml', 'xml', or 'plaintext'
    decorator = f"OutputFormat(format='{format}')"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def tone(style: str = "technical") -> None:
    """Demonstrate the Tone decorator"""
    log_info(f"Running Tone example with style={style}")
    prompt = "Explain what is cloud computing."
    # Ensure style is one of: 'formal', 'casual', 'friendly', 'technical', or 'humorous'
    decorator = f"Tone(style='{style}')"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def audience(level: str = "beginner") -> None:
    """Demonstrate the Audience decorator"""
    log_info(f"Running Audience example with level={level}")
    prompt = "Explain how neural networks work."
    # Ensure level is one of: 'beginner', 'intermediate', 'expert', or 'technical'
    decorator = f"Audience(level='{level}')"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def concise(
    level: str = "moderate",
    max_words: Optional[int] = None,
    bullet_points: bool = False,
) -> None:
    """Demonstrate the Concise decorator"""
    log_info(f"Running Concise example with level={level}")
    prompt = "Explain the difference between machine learning and deep learning."

    # Build the decorator string conditionally based on parameters
    parameters = []
    if level:
        # Ensure level is one of: 'moderate', 'high', or 'extreme'
        parameters.append(f"level='{level}'")
    if max_words and max_words >= 10 and max_words <= 500:
        parameters.append(f"maxWords={max_words}")
    if bullet_points is not None:
        parameters.append(f"bulletPoints={str(bullet_points).lower()}")

    decorator = f"Concise({', '.join(parameters)})"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def detailed(depth: str = "comprehensive", examples: bool = True) -> None:
    """Demonstrate the Detailed decorator"""
    log_info(f"Running Detailed example with depth={depth}")
    prompt = "Explain the concept of containerization in software development."

    # Build the decorator string conditionally based on parameters
    parameters = []
    # Ensure depth is one of: 'moderate', 'comprehensive', or 'exhaustive'
    parameters.append(f"depth='{depth}'")
    parameters.append(f"examples={str(examples).lower()}")

    decorator = f"Detailed({', '.join(parameters)})"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def negative_space() -> None:
    """Demonstrate the NegativeSpace decorator"""
    log_info("Running NegativeSpace example")
    prompt = "Discuss the future of remote work."
    decorator = "NegativeSpace()"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def bullet(style: str = "dash", indented: bool = True, compact: bool = False) -> None:
    """Demonstrate the Bullet decorator"""
    log_info(f"Running Bullet example with style={style}")
    prompt = "List the benefits of adopting microservices architecture."

    # Build the decorator string conditionally based on parameters
    parameters = []
    # Ensure style is one of: 'dash', 'dot', 'arrow', 'star', or 'plus'
    parameters.append(f"style='{style}'")
    parameters.append(f"indented={str(indented).lower()}")
    parameters.append(f"compact={str(compact).lower()}")

    decorator = f"Bullet({', '.join(parameters)})"
    result = query_with_decorators(prompt, [decorator])


@app.command()
def tree_of_thought(branches: int = 3, depth: int = 3, pruning: bool = False) -> None:
    """Demonstrate the TreeOfThought decorator"""
    log_info(f"Running TreeOfThought example with branches={branches}, depth={depth}")
    prompt = "What strategies could help reduce carbon emissions?"

    # Build the decorator string conditionally based on parameters
    parameters = []
    parameters.append(f"branches={branches}")
    parameters.append(f"depth={depth}")
    parameters.append(f"pruning={str(pruning).lower()}")

    decorator = f"TreeOfThought({', '.join(parameters)})"
    result = query_with_decorators(prompt, [decorator])


if __name__ == "__main__":
    app()
