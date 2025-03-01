#!/usr/bin/env python3
"""Setup script for the Prompt Decorators Core extension package."""

from setuptools import setup, find_packages

setup(
    name="prompt-decorators-core",
    version="1.0.0",
    description="Core decorators for the Prompt Decorators standard",
    author="Prompt Decorators Working Group",
    author_email="spec@promptdecorators.ai",
    url="https://github.com/prompt-decorators/spec",
    packages=find_packages(),
    py_modules=["python_implementation"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    package_data={
        "": ["README.md", "package.json", "examples/*.md"],
    },
    entry_points={
        "console_scripts": [
            "prompt-decorators-demo=python_implementation:main",
        ],
    },
) 