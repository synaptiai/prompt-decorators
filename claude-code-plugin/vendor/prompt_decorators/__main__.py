#!/usr/bin/env python3
"""CLI interface for prompt-decorators package verification and utilities.

This module provides command-line tools for verifying the installation,
diagnosing registry issues, and performing maintenance operations.

Usage:
    python -m prompt_decorators verify
    python -m prompt_decorators verify --detailed
    python -m prompt_decorators repair --auto
    python -m prompt_decorators info
"""

import argparse
import sys
from typing import Any, Dict, cast  # Added cast


def cmd_verify(args: argparse.Namespace) -> int:
    """Verify the prompt-decorators installation."""
    try:
        from prompt_decorators.core.dynamic_decorator import DynamicDecorator
        from prompt_decorators.utils.registry_validator import RegistryValidator

        print("🔍 Verifying prompt-decorators installation...")

        # Get registry information
        registry_info = RegistryValidator.get_registry_info()

        # Basic verification
        print(f"\n📊 Registry Status:")
        print(f"  Package registry exists: {registry_info['package_registry_exists']}")
        print(f"  Source registry exists: {registry_info['source_registry_exists']}")
        print(f"  Package registry files: {registry_info['package_file_count']}")
        print(f"  Source registry files: {registry_info['source_file_count']}")

        # Try to load decorators
        print(f"\n🔄 Loading decorators...")
        DynamicDecorator._loaded = False  # Force reload
        DynamicDecorator.load_registry()

        decorator_count = len(DynamicDecorator._registry)
        print(f"  Decorators loaded: {decorator_count}")

        if decorator_count == 0:
            print("❌ No decorators loaded - installation may be incomplete")
            return 1

        # Show sample decorators
        if args.detailed:
            print(f"\n📋 Available decorators:")
            for i, (name, definition) in enumerate(DynamicDecorator._registry.items()):
                if i >= 10:  # Limit to first 10
                    print(f"  ... and {decorator_count - 10} more")
                    break
                category = definition.get("category", "Unknown")
                description = definition.get("description", "No description")[:60]
                print(f"  {name} ({category}): {description}")
        else:
            sample_names = list(DynamicDecorator._registry.keys())[:5]
            print(f"  Sample decorators: {sample_names}")

        # Validation check
        print(f"\n✅ Validation:")
        validation_result = RegistryValidator.validate_registry()

        if validation_result["status"] == "healthy":
            print("  Registry status: Healthy ✅")
        elif validation_result["status"] == "needs_repair":
            print("  Registry status: Needs repair ⚠️")
            if args.detailed:
                for issue in validation_result.get("issues", []):
                    print(f"    - {issue}")
        else:
            print("  Registry status: Critical issues ❌")
            if args.detailed:
                for issue in validation_result.get("issues", []):
                    print(f"    - {issue}")

        print(f"\n🎉 Installation verification completed successfully!")
        return 0

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("The prompt-decorators package may not be properly installed.")
        return 1
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return 1


def cmd_repair(args: argparse.Namespace) -> int:
    """Repair the registry installation."""
    try:
        from prompt_decorators.utils.registry_validator import RegistryValidator

        print("🔧 Repairing prompt-decorators registry...")

        if args.auto:
            success, message = RegistryValidator.auto_repair_registry()
            if success:
                print(f"✅ Auto-repair successful: {message}")
                return 0
            else:
                print(f"❌ Auto-repair failed: {message}")
                return 1
        else:
            # Interactive repair (future enhancement)
            print("Interactive repair not yet implemented. Use --auto flag.")
            return 1

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return 1
    except Exception as e:
        print(f"❌ Repair failed: {e}")
        return 1


def cmd_info(args: argparse.Namespace) -> int:
    """Show detailed information about the installation."""
    try:
        import prompt_decorators
        from prompt_decorators.utils.registry_validator import RegistryValidator

        print("📋 Prompt Decorators Installation Information")
        print("=" * 50)

        # Package information
        print(
            f"Package version: {getattr(prompt_decorators, '__version__', 'Unknown')}"
        )
        print(f"Package location: {prompt_decorators.__file__}")

        # Registry information
        registry_info = RegistryValidator.get_registry_info()
        print(f"\n📁 Registry Information:")
        for key, value in registry_info.items():
            print(f"  {key}: {value}")

        # System information
        print(f"\n🖥️  System Information:")
        print(f"  Python version: {sys.version}")
        print(f"  Platform: {sys.platform}")

        return 0

    except Exception as e:
        print(f"❌ Failed to get information: {e}")
        return 1


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="prompt-decorators", description="Prompt Decorators CLI utilities"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify installation")
    verify_parser.add_argument(
        "--detailed", action="store_true", help="Show detailed verification information"
    )
    verify_parser.set_defaults(func=cmd_verify)

    # Repair command
    repair_parser = subparsers.add_parser("repair", help="Repair registry issues")
    repair_parser.add_argument(
        "--auto", action="store_true", help="Automatically repair registry issues"
    )
    repair_parser.set_defaults(func=cmd_repair)

    # Info command
    info_parser = subparsers.add_parser("info", help="Show installation information")
    info_parser.set_defaults(func=cmd_info)

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Execute command
    return cast(int, args.func(args))  # Added cast here


if __name__ == "__main__":
    sys.exit(main())
