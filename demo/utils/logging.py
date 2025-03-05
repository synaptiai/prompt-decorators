"""
Logging utilities for the OpenAI prompt decorator demo.

This module provides logging functionality with rich formatting
for better visual representation of prompts and responses.
"""

import json
from typing import Any, Dict, Optional

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

# Initialize console
console = Console()


def log_final_prompt(prompt: str) -> None:
    """
    Log the final prompt.
    """
    console.print(Panel(prompt, title="Final Prompt", border_style="green"))


def log_decorated_prompt(
    original_prompt: str, decorator_str: str, transformed_prompt: str
) -> None:
    """
    Log a comparison between original prompt, decorator syntax, and the transformed prompt.

    Args:
        original_prompt: The original prompt before decoration
        decorator_str: The decorator string (e.g., "Reasoning(depth='comprehensive')")
        transformed_prompt: The final transformed prompt with applied decorations
    """
    # Create a table for the syntax comparison (original vs decorator syntax)
    syntax_table = Table(
        show_header=True,
        header_style="bold magenta",
        title="Original vs Decorator Syntax",
    )

    # Add columns for the syntax comparison
    syntax_table.add_column("Original Prompt", style="cyan", justify="left")
    syntax_table.add_column("→", style="yellow", justify="center", width=3)
    syntax_table.add_column("Decorated Prompt", style="green", justify="left")

    # Add the row with the syntax comparison
    syntax_table.add_row(original_prompt, "→", f"{decorator_str}\n{original_prompt}")

    # Create table for the transformation comparison (original vs transformed)
    transform_table = Table(
        show_header=True,
        header_style="bold magenta",
        title="Original vs Transformed Prompt",
    )

    # Add columns for the transformation comparison
    transform_table.add_column("Original Prompt", style="cyan", justify="left")
    transform_table.add_column("→", style="yellow", justify="center", width=3)
    transform_table.add_column("Decorated Prompt", style="green", justify="left")

    # Add the row with the transformation comparison
    transform_table.add_row(original_prompt, "→", transformed_prompt)

    # Print both comparisons with clear titles
    console.print(Panel(syntax_table, border_style="yellow"))
    console.print(Panel(transform_table, border_style="yellow"))


def log_response(response: Any, title: str = "Response") -> None:
    """
    Log a response with nice formatting.

    Args:
        response: The response to log (string, dict, or OpenAI response object)
        title: Title for the panel containing the response
    """
    if hasattr(response, "choices") and hasattr(response.choices[0], "message"):
        # This is an OpenAI API response object
        content = response.choices[0].message.content
    elif isinstance(response, dict):
        if "content" in response:
            # This is our response dictionary, display the actual content
            content = response["content"]
            # Also show usage statistics in a smaller format below the content
            stats = (
                f"\n\n[dim]Model: {response.get('model', 'unknown')} | "
                f"Tokens: {response.get('total_tokens', 'unknown')} "
                f"({response.get('prompt_tokens', '?')}/{response.get('completion_tokens', '?')})[/dim]"
            )
            content = content + stats
        else:
            # This is some other dictionary, format as JSON
            content = json.dumps(response, indent=2)
            content = Syntax(content, "json", theme="monokai", line_numbers=True)
    else:
        # Assume it's a string
        content = str(response)

    console.print(Panel(content, title=title, border_style="green"))


def log_comparison(
    original: str, decorated: str, title: str = "Prompt Comparison"
) -> None:
    """
    Log a comparison between original and decorated prompts.

    Args:
        original: The original prompt
        decorated: The decorated prompt
        title: Title for the comparison
    """
    # Create a table with clear titles and styling
    table = Table(title=title, show_header=True, header_style="bold magenta")

    # Add columns with better styling
    table.add_column("Original Prompt", style="cyan", justify="left")
    table.add_column("→", style="yellow", justify="center", width=3)
    table.add_column("Decorated Prompt", style="green", justify="left")

    # Add a visual indicator to highlight the added decorators
    decorators_part = (
        decorated[: decorated.find(original)].strip()
        if original in decorated
        else decorated
    )
    original_part = original
    remaining_part = ""

    if original in decorated:
        remaining_part = decorated[decorated.find(original) + len(original) :].strip()

    # Format decorated prompt to highlight the decorators
    if decorators_part or remaining_part:
        formatted_decorated = decorated
    else:
        formatted_decorated = decorated

    # Add the row with the comparison
    table.add_row(original_part, "→", formatted_decorated)

    # Print the comparison table
    console.print(Panel(table, border_style="yellow"))


def log_error(message: str) -> None:
    """
    Log an error message.

    Args:
        message: The error message to log
    """
    console.print(f"[bold red]ERROR:[/bold red] {message}")


def log_info(message: str) -> None:
    """
    Log an informational message.

    Args:
        message: The message to log
    """
    console.print(f"[bold blue]INFO:[/bold blue] {message}")
