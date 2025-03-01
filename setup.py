"""
Setup script for the Prompt Decorators package.
"""

import os
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Define package metadata
setup(
    name="prompt-decorators",
    version="0.1.0",
    description="A framework for defining, managing, and applying prompt decorators to enhance interactions with LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Bentes",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/prompt-decorators",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    package_data={
        "prompt_decorators": ["py.typed"],  # For PEP 561 compliance
        "prompt_decorators.registry": ["*.json"],  # Include registry JSON files
    },
    include_package_data=True,
    python_requires=">=3.8",
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
            "ruff>=0.0.267",
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings>=0.22.0",
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
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="llm, prompt engineering, nlp, ai, language models, decorators",
    project_urls={
        "Documentation": "https://yourusername.github.io/prompt-decorators/",
        "Source": "https://github.com/yourusername/prompt-decorators",
        "Issue Tracker": "https://github.com/yourusername/prompt-decorators/issues",
    },
) 