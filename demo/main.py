"""
Main entry point for the OpenAI Prompt Decorator Demo.

This module integrates all the example modules and provides a unified CLI interface.
"""

from typing import Optional

import typer

from demo.examples.advanced import app as advanced_app
from demo.examples.basic import app as basic_app
from demo.examples.domain_specific import app as domain_app
from demo.openai_demo import app as openai_app

# Use absolute imports rather than relative imports
from demo.utils.logging import log_info

app = typer.Typer(
    help="OpenAI Prompt Decorator Demo - Showcase the power of prompt decorators with OpenAI"
)

# Add all sub-applications
app.add_typer(
    openai_app, name="custom", help="Run custom prompts with decorators of your choice"
)
app.add_typer(basic_app, name="basic", help="Basic decorator examples")
app.add_typer(
    advanced_app, name="advanced", help="Advanced decorator composition examples"
)
app.add_typer(domain_app, name="domain", help="Domain-specific decorator examples")


@app.callback()
def main() -> None:
    """
    OpenAI Prompt Decorator Demo - Showcase the power of prompt decorators with OpenAI.

    This application demonstrates how to use prompt decorators with the OpenAI API
    to enhance LLM outputs across various use cases. The demo includes basic examples,
    advanced compositions, and domain-specific applications.
    """
    log_info("Starting Prompt Decorators Demo")


@app.command()
def version() -> None:
    """
    Show version information for the demo.
    """
    log_info("Prompt Decorators Demo v1.0.0")
    log_info(
        "For more information, visit: https://github.com/synaptiai/prompt-decorators"
    )


if __name__ == "__main__":
    app()
