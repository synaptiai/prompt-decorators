"""
Setup script for the Prompt Decorators package.
"""

import os
import subprocess
import sys
from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.install import install


# Custom commands to run the registry setup and copy scripts
class PreBuildCommand(build_py):
    """Pre-build command to copy registry files."""

    def run(self) -> None:
        """Run the pre-build command.

        Returns:
            None
        """
        self.execute_copy_registry()
        build_py.run(self)

def execute_copy_registry() -> None:
    """Execute the copy registry script.
    Returns:
        None
    """
    try:
        copy_script = Path(__file__).parent / "scripts" / "copy_registry.py"
        if copy_script.exists():
            print("Running copy registry script...")
            subprocess.check_call([sys.executable, str(copy_script)])
        else:
            print(f"Copy registry script not found: {copy_script}")
    except Exception as e:
        print(f"Error running copy registry script: {e}")
        self.execute_registry_setup()

    def execute_copy_registry(self) -> None:
        """Execute the copy registry script.

        Returns:
            None
        """
        try:
            copy_script = Path(__file__).parent / "scripts" / "copy_registry.py"
            if copy_script.exists():
                print("Running copy registry script...")
                subprocess.check_call([sys.executable, str(copy_script)])
            else:
                print(f"Copy registry script not found: {copy_script}")
        except Exception as e:
            print(f"Error running copy registry script: {e}")

    def execute_registry_setup(self) -> None:
        """Execute the registry setup script.

        Returns:
            None
        """
        try:
            setup_script = Path(__file__).parent / "scripts" / "setup_registry.py"
            if setup_script.exists():
                print("Running registry setup script...")
                subprocess.check_call([sys.executable, str(setup_script)])
            else:
                print(f"Registry setup script not found: {setup_script}")
        except Exception as e:
            print(f"Error running registry setup script: {e}")


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self) -> None:
        """Run the post-install command.

        Returns:
            None
        """
        install.run(self)
        self.execute_registry_setup()

    def execute_registry_setup(self) -> None:
        """Execute the registry setup script.

        Returns:
            None
        """
        try:
            setup_script = Path(__file__).parent / "scripts" / "setup_registry.py"
            if setup_script.exists():
                print("Running registry setup script...")
                subprocess.check_call([sys.executable, str(setup_script)])
            else:
                print(f"Registry setup script not found: {setup_script}")
        except Exception as e:
            print(f"Error running registry setup script: {e}")


# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Define package metadata
setup(
    name="prompt-decorators",
    version="0.3.1",
    description="A framework for defining, managing, and applying prompt decorators to enhance interactions with LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Bentes",
    author_email="promptdecorators@synapti.ai",
    url="https://github.com/synaptiai/prompt-decorators",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    package_data={
        "prompt_decorators": ["py.typed"],  # For PEP 561 compliance
        "prompt_decorators.registry": [
            "**/*.json"
        ],  # Include all registry JSON files recursively
        "prompt_decorators.registry.core": ["**/*.json"],  # Core decorators
        "prompt_decorators.registry.extensions": ["**/*.json"],  # Extension decorators
        "prompt_decorators.registry.simplified_decorators": [
            "**/*.json",
            "**/*.yml",
        ],  # Simplified decorators
    },
    include_package_data=True,
    python_requires=">=3.11",
    install_requires=[
        "pydantic>=2.0.0",
        "typing_extensions>=4.0.0",
        "jsonschema>=4.0.0",
        "importlib-metadata>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
            "ruff>=0.1.0",
            "pre-commit>=4.1.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.0.0",
            "mkdocs-awesome-pages-plugin>=2.9.0",
            "mkdocs-autolinks-plugin>=0.7.0",
            "mkdocs-git-revision-date-localized-plugin>=1.2.0",
            "mkdocstrings>=0.24.0",
            "mkdocstrings-python>=1.0.0",
        ],
        "langchain": [
            "langchain>=0.0.200",
        ],
        "openai": [
            "openai>=1.0.0",
        ],
        "anthropic": [
            "anthropic>=0.5.0",
        ],
        "mcp": [
            "mcp[cli]>=0.1.0",
        ],
        "all": [
            "langchain>=0.0.200",
            "openai>=1.0.0",
            "anthropic>=0.5.0",
            "mcp[cli]>=0.1.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="llm, prompt engineering, nlp, ai, language models, decorators",
    project_urls={
        "Documentation": "https://synaptiai.github.io/prompt-decorators/",
        "Source": "https://github.com/synaptiai/prompt-decorators",
        "Issue Tracker": "https://github.com/synaptiai/prompt-decorators/issues",
    },
    cmdclass={
        "build_py": PreBuildCommand,
        "develop": PostDevelopCommand,
        "install": PostInstallCommand,
    },
)
