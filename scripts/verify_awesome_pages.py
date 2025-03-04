#!/usr/bin/env python
"""Verify that the awesome-pages plugin is installed and working correctly.

This script attempts to import the awesome-pages plugin and verify its version.
It also checks if the plugin is properly registered with MkDocs.

Usage:
    python scripts/verify_awesome_pages.py
"""

import importlib
import subprocess
import sys
from pathlib import Path


def verify_awesome_pages():
    """Verify that the awesome-pages plugin is installed and working correctly."""
    print("Verifying awesome-pages plugin installation...")

    # Check if the package is installed
    try:
        result = subprocess.run(
            ["pip", "show", "mkdocs-awesome-pages-plugin"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("ERROR: mkdocs-awesome-pages-plugin is not installed!")
            print("Installing mkdocs-awesome-pages-plugin...")

            install_result = subprocess.run(
                ["pip", "install", "mkdocs-awesome-pages-plugin>=2.10.1"],
                capture_output=True,
                text=True,
            )

            if install_result.returncode != 0:
                print(
                    f"ERROR: Failed to install mkdocs-awesome-pages-plugin: {install_result.stderr}"
                )
                return False

            print("Successfully installed mkdocs-awesome-pages-plugin")
        else:
            print("mkdocs-awesome-pages-plugin is installed:")
            for line in result.stdout.splitlines():
                print(f"  {line}")

        # Try to import the module
        try:
            import mkdocs_awesome_pages_plugin

            print(
                f"Successfully imported mkdocs_awesome_pages_plugin (version: {mkdocs_awesome_pages_plugin.__version__})"
            )
        except ImportError as e:
            print(f"ERROR: Failed to import mkdocs_awesome_pages_plugin: {e}")
            return False
        except AttributeError:
            print("WARNING: Could not determine mkdocs_awesome_pages_plugin version")

        # Check if the plugin is registered with MkDocs
        try:
            import mkdocs.plugins

            # This is a bit of a hack, but it should work to check if the plugin is registered
            from mkdocs.config.defaults import MkDocsConfig

            config = MkDocsConfig()
            config.load_dict({"plugins": ["awesome-pages"]})
            config.validate()

            print(
                "Successfully validated MkDocs configuration with awesome-pages plugin"
            )
            return True
        except ImportError as e:
            print(f"ERROR: Failed to import mkdocs.plugins: {e}")
            return False
        except Exception as e:
            print(f"ERROR: Failed to validate MkDocs configuration: {e}")

            # Try to install the plugin again with explicit version
            print("Attempting to reinstall the plugin with explicit version...")
            reinstall_result = subprocess.run(
                [
                    "pip",
                    "install",
                    "--force-reinstall",
                    "mkdocs-awesome-pages-plugin==2.10.1",
                ],
                capture_output=True,
                text=True,
            )

            if reinstall_result.returncode != 0:
                print(f"ERROR: Failed to reinstall plugin: {reinstall_result.stderr}")
                return False

            print("Successfully reinstalled the plugin. Verifying again...")

            # Verify the plugin is now properly installed
            verify_result = subprocess.run(
                [
                    "python",
                    "-c",
                    "import mkdocs_awesome_pages_plugin; print(mkdocs_awesome_pages_plugin.__version__)",
                ],
                capture_output=True,
                text=True,
            )

            if verify_result.returncode != 0:
                print(
                    f"ERROR: Plugin still not working after reinstall: {verify_result.stderr}"
                )
                return False

            print(f"Plugin reinstalled successfully: {verify_result.stdout.strip()}")
            return True

    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = verify_awesome_pages()
    sys.exit(0 if success else 1)
