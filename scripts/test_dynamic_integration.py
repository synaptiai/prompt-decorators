#!/usr/bin/env python
"""
Script to test the dynamic integration of prompt decorators.

This script verifies that the dynamic implementation works correctly,
including the MCP dynamic integration.
"""

import logging
import sys
from typing import Any, Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def test_dynamic_decorator_import() -> bool:
    """Test importing the dynamic decorator classes."""
    try:
        from prompt_decorators.core.base import DecoratorBase, DecoratorParameter
        from prompt_decorators.core.dynamic_decorator import DynamicDecorator
        from prompt_decorators.dynamic_decorators_module import (
            apply_dynamic_decorators,
            create_decorator_instance,
            get_available_decorators,
        )

        logger.info(f"✅ Successfully imported dynamic decorator modules")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to import dynamic decorator modules: {e}")
        return False


def test_list_available_decorators() -> bool:
    """Test listing available decorators."""
    try:
        from prompt_decorators.dynamic_decorators_module import get_available_decorators

        decorators = get_available_decorators()
        logger.info(
            f"✅ Found {len(decorators)} decorators, including: "
            f"{', '.join([d.name for d in decorators[:5]])}"
        )
        return True
    except Exception as e:
        logger.error(f"❌ Failed to list available decorators: {e}")
        return False


def test_create_decorator() -> bool:
    """Test creating a decorator instance."""
    try:
        from prompt_decorators.dynamic_decorators_module import (
            create_decorator_instance,
        )

        decorator = create_decorator_instance("StepByStep", numbered=True)
        logger.info(f"✅ Successfully created decorator: {decorator}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to create decorator: {e}")
        return False


def test_transform_prompt() -> bool:
    """Test transforming a prompt with decorators."""
    try:
        from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators

        prompt = "+++StepByStep(numbered=true)\nHow do I build a website?"
        transformed = apply_dynamic_decorators(prompt)
        logger.info(f"✅ Successfully transformed prompt")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to transform prompt: {e}")
        return False


def test_decorator_application() -> bool:
    """Test applying a decorator to a prompt."""
    try:
        from prompt_decorators.dynamic_decorators_module import (
            create_decorator_instance,
        )

        decorator = create_decorator_instance("StepByStep", numbered=True)
        prompt = "How do I build a website?"
        transformed = decorator(prompt)
        logger.info(f"✅ Successfully applied decorator to prompt")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to apply decorator: {e}")
        return False


def test_mcp_dynamic_import() -> bool:
    """Test importing the MCP dynamic integration."""
    try:
        from prompt_decorators.integrations.mcp_dynamic import (
            create_default_templates,
            create_mcp_server,
        )

        logger.info(f"✅ Successfully imported MCP dynamic integration")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to import MCP dynamic integration: {e}")
        return False


def test_mcp_create_server() -> bool:
    """Test creating an MCP server."""
    try:
        from prompt_decorators.integrations.mcp_dynamic import create_mcp_server

        server = create_mcp_server("test-server")
        logger.info(f"✅ Successfully created MCP server")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to create MCP server: {e}")
        return False


def test_mcp_templates() -> bool:
    """Test creating default templates for the MCP integration."""
    try:
        from prompt_decorators.integrations.mcp_dynamic import create_default_templates

        templates = create_default_templates()
        logger.info(f"✅ Successfully created {len(templates)} default templates")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to create default templates: {e}")
        return False


def main() -> None:
    """Run all tests and report results."""
    logger.info("Starting dynamic integration tests...")

    # Run all tests
    tests = [
        test_dynamic_decorator_import,
        test_list_available_decorators,
        test_create_decorator,
        test_transform_prompt,
        test_decorator_application,
        test_mcp_dynamic_import,
        test_mcp_create_server,
        test_mcp_templates,
    ]

    # Track results
    results = []
    for test in tests:
        results.append(test())

    # Report results
    logger.info("=" * 50)
    logger.info(f"Test Results: {sum(results)}/{len(results)} passed")
    logger.info("=" * 50)

    # Exit with appropriate code
    if all(results):
        logger.info("All tests passed!")
        sys.exit(0)
    else:
        logger.error("Some tests failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
