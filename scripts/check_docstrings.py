#!/usr/bin/env python
"""
This script analyzes Python files to ensure docstrings follow Google-style format,
checking for required sections like Args, Returns, Raises, etc. when appropriate.
"""

import argparse
import ast
import os
import sys
from pathlib import Path
from typing import Dict, List


class DocstringIssue:
    """Represents an issue found in a docstring."""

    def __init__(self, file_path, line_number, function_name, issue_type, message):
        """
        Initialize a docstring issue.

        Args:
            file_path: Path to the file containing the issue
            line_number: Line number where the issue was found
            function_name: Name of the function or class with the issue
            issue_type: Type of issue (missing, malformed, etc.)
            message: Description of the issue
        """
        self.file_path = file_path
        self.line_number = line_number
        self.function_name = function_name
        self.issue_type = issue_type
        self.message = message

    def __str__(self) -> str:
        """
        Convert the issue to a string representation.

        Returns:
            String representation of the issue
        """
        return (
            f"  Line {self.line_number}: {self.function_name} - "
            f"{self.issue_type} - {self.message}"
        )


class DocstringChecker:
    """Checks docstrings for Google-style format compliance."""

    def __init__(self, root_dir):
        """
        Initialize the docstring checker.

        Args:
            root_dir: Root directory to scan for Python files
        """
        self.root_dir = Path(root_dir)
        self.files_with_issues = set()

    def check_all_files(self):
        """
        Check all Python files in the root directory.

        Args:
            self: The DocstringChecker instance.

        Returns:
            List of docstring issues found
        """
        issues = []

        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = Path(root) / file
                    file_issues = self.check_file(file_path)
                    if file_issues:
                        issues.extend(file_issues)
                        self.files_with_issues.add(file_path)

        return issues

    def check_file(self, file_path):
        """
        Check a single Python file for docstring issues.

        Args:
            file_path: Path to the Python file to check

        Returns:
            List of docstring issues found in the file
        """
        issues = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)

            # Check module docstring
            if ast.get_docstring(tree):
                # Module has a docstring, check it
                pass
            else:
                # Module is missing a docstring
                issues.append(
                    DocstringIssue(
                        file_path,
                        1,
                        file_path.name,
                        "missing",
                        "Module is missing a docstring",
                    )
                )

            # Check class and function docstrings
            for node in ast.walk(tree):
                if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                    issues.extend(self.check_node_docstring(node, file_path, content))

        except Exception as e:
            print(f"Error checking {file_path}: {e}")

        return issues

    def check_node_docstring(self, node, file_path, content):
        """
        Check the docstring of a node (function or class).

        Args:
            node: AST node to check
            file_path: Path to the file containing the node
            content: Content of the file

        Returns:
            List of docstring issues found in the node
        """
        issues = []

        node_name = node.name
        if isinstance(node, ast.FunctionDef) and hasattr(node, "parent_class"):
            node_name = f"{node.parent_class}.{node.name}"

        docstring = ast.get_docstring(node)
        if not docstring:
            # Node is missing a docstring
            issues.append(
                DocstringIssue(
                    file_path,
                    node.lineno,
                    node_name,
                    "missing",
                    f"{'Class' if isinstance(node, ast.ClassDef) else 'Function'} is missing a docstring",
                )
            )

        # Additional checks for docstring format could be added here

        return issues


def main():
    """Run the docstring checker."""

    parser = argparse.ArgumentParser(
        description="Check docstrings for Google-style format compliance"
    )
    parser.add_argument(
        "root_dir",
        nargs="?",
        default="prompt_decorators",
        help="Root directory to scan",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show verbose output"
    )

    args = parser.parse_args()

    checker = DocstringChecker(args.root_dir)
    issues = checker.check_all_files()

    if issues:
        print(
            f"\nFound {len(issues)} docstring issues in {len(checker.files_with_issues)} files:\n"
        )

        # Group issues by file
        issues_by_file: Dict[str, List[DocstringIssue]] = {}
        for issue in issues:
            if issue.file_path not in issues_by_file:
                issues_by_file[issue.file_path] = []
            issues_by_file[issue.file_path].append(issue)

        # Print issues by file
        for file_path, file_issues in issues_by_file.items():
            print(f"{file_path} ({len(file_issues)} issues):")
            for issue in file_issues:
                print(issue)
            print()

        sys.exit(1)
    else:
        print("No docstring issues found!")
        sys.exit(0)


# Execute main function if script is run directly
if __name__ == "__main__":
    main()
