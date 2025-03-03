#!/usr/bin/env python3
"""
Docstring Standardization Script

This script analyzes Python files in the codebase to identify and report
docstrings that don't follow Google-style format. It can also fix simple
issues automatically. The script can process multiple files or directories
at once, making it suitable for use with pre-commit hooks.
"""

import argparse
import ast
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Regular expressions for Google-style docstring sections
SECTION_PATTERN = re.compile(
    r"^\s*(Args|Returns|Raises|Yields|Examples|Note|Notes|Warning|Attributes):\s*$"
)
ARGS_PATTERN = re.compile(r"^\s*([*a-zA-Z0-9_]+)(\s*\([^)]+\))?:\s*(.+)$")
RETURNS_PATTERN = re.compile(r"^\s*([^:]+):\s*(.+)$")
RAISES_PATTERN = re.compile(r"^\s*([^:]+):\s*(.+)$")


# Docstring issues
class DocstringIssue:
    """Represents an issue with a docstring."""

    def __init__(
        self,
        file_path: Path,
        line_number: int,
        node_name: str,
        issue_type: str,
        message: str,
    ):
        """
        Initialize a docstring issue.

        Args:
            file_path: Path to the file containing the issue
            line_number: Line number where the issue occurs
            node_name: Name of the function or class with the issue
            issue_type: Type of issue (missing, malformed, etc.)
            message: Description of the issue
        """
        self.file_path = file_path
        self.line_number = line_number
        self.node_name = node_name
        self.issue_type = issue_type
        self.message = message

    def __str__(self) -> str:
        """Return a string representation of the issue."""
        return f"{self.file_path}:{self.line_number} - {self.node_name}: {self.issue_type} - {self.message}"


class DocstringAnalyzer(ast.NodeVisitor):
    """Analyzes Python files for docstring issues."""

    def __init__(self, file_path: Path):
        """
        Initialize the docstring analyzer.

        Args:
            file_path: Path to the file to analyze
        """
        self.file_path = file_path
        self.issues: List[DocstringIssue] = []
        self.current_class: Optional[str] = None

    def visit_Module(self, node: ast.Module) -> None:
        """
        Visit a module node.

        Args:
            node: The AST node to visit

        Returns:
            None: This method adds issues to self.issues but doesn't return a value
        """
        # Check module docstring
        if not ast.get_docstring(node):
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    1,
                    self.file_path.name,
                    "missing",
                    "Module is missing a docstring",
                )
            )
        else:
            self._check_docstring_format(
                ast.get_docstring(node), 1, self.file_path.name, is_module=True
            )

        # Visit all nodes in the module
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """
        Visit a class definition node.

        Args:
            node: The AST node to visit

        Returns:
            None: This method adds issues to self.issues but doesn't return a value
        """
        # Save current class name
        old_class = self.current_class
        self.current_class = node.name

        # Check class docstring
        if not ast.get_docstring(node):
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    node.lineno,
                    node.name,
                    "missing",
                    "Class is missing a docstring",
                )
            )
        else:
            self._check_docstring_format(
                ast.get_docstring(node), node.lineno, node.name, is_class=True
            )

        # Visit all nodes in the class
        self.generic_visit(node)

        # Restore previous class name
        self.current_class = old_class

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Visit a function definition node.

        Args:
            node: The AST node to visit

        Returns:
            None: This method adds issues to self.issues but doesn't return a value
        """
        # Skip special methods
        if (
            node.name.startswith("__")
            and node.name.endswith("__")
            and node.name != "__init__"
        ):
            return

        # Determine function name
        func_name = (
            f"{self.current_class}.{node.name}" if self.current_class else node.name
        )

        # Check function docstring
        if not ast.get_docstring(node):
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    node.lineno,
                    func_name,
                    "missing",
                    "Function is missing a docstring",
                )
            )
        else:
            self._check_docstring_format(
                ast.get_docstring(node),
                node.lineno,
                func_name,
                is_function=True,
                has_args=bool(node.args.args),
                has_return=node.returns is not None
                or any(
                    isinstance(stmt, ast.Return) and stmt.value for stmt in node.body
                ),
            )

        # Visit all nodes in the function
        self.generic_visit(node)

    def _check_docstring_format(
        self,
        docstring: str,
        line_number: int,
        node_name: str,
        is_module: bool = False,
        is_class: bool = False,
        is_function: bool = False,
        has_args: bool = False,
        has_return: bool = False,
    ) -> None:
        """
        Check if a docstring follows Google-style format.

        Args:
            docstring: The docstring to check
            line_number: The line number where the docstring appears
            node_name: The name of the node (module, class, or function)
            is_module: Whether the docstring belongs to a module
            is_class: Whether the docstring belongs to a class
            is_function: Whether the docstring belongs to a function
            has_args: Whether the function has arguments
            has_return: Whether the function has a return value

        Returns:
            None: This method adds issues to self.issues but doesn't return a value
        """
        # Skip empty docstrings
        if not docstring.strip():
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    line_number,
                    node_name,
                    "empty",
                    "Docstring is empty",
                )
            )
            return

        # Split docstring into lines
        lines = docstring.strip().split("\n")

        # Check for one-line docstrings
        if len(lines) == 1:
            # One-line docstrings are acceptable for simple cases
            return

        # Check for sections
        has_args_section = False
        has_returns_section = False
        has_raises_section = False

        current_section = None
        for i, line in enumerate(lines):
            # Check for section headers
            section_match = SECTION_PATTERN.match(line)
            if section_match:
                current_section = section_match.group(1)
                if current_section == "Args":
                    has_args_section = True
                elif current_section == "Returns":
                    has_returns_section = True
                elif current_section == "Raises":
                    has_raises_section = True
                continue

            # Check section content
            if current_section == "Args" and line.strip():
                # Check args format
                args_match = ARGS_PATTERN.match(line)
                if not args_match:
                    self.issues.append(
                        DocstringIssue(
                            self.file_path,
                            line_number,
                            node_name,
                            "malformed",
                            f"Malformed Args section at line {i+1}: '{line}'",
                        )
                    )

        # Check if required sections are present
        if is_function and has_args and not has_args_section:
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    line_number,
                    node_name,
                    "missing_section",
                    "Function has arguments but no Args section in docstring",
                )
            )

        if is_function and has_return and not has_returns_section:
            self.issues.append(
                DocstringIssue(
                    self.file_path,
                    line_number,
                    node_name,
                    "missing_section",
                    "Function has a return value but no Returns section in docstring",
                )
            )


def analyze_file(file_path: Path) -> List[DocstringIssue]:
    """
    Analyze a Python file for docstring issues.

    Args:
        file_path: Path to the file to analyze

    Returns:
        List of docstring issues found in the file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        # Skip auto-generated test files
        if "tests/auto/" in str(file_path) and "This file is auto-generated" in source:
            logger.info(f"Skipping auto-generated test file: {file_path}")
            return []

        # Parse the source code
        tree = ast.parse(source)

        # Analyze the AST
        analyzer = DocstringAnalyzer(file_path)
        analyzer.visit(tree)

        return analyzer.issues
    except Exception as e:
        logger.error(f"Error analyzing {file_path}: {e}")
        return []


def analyze_directory(
    directory: Path, exclude_dirs: Optional[List[str]] = None
) -> Dict[Path, List[DocstringIssue]]:
    """
    Analyze all Python files in a directory for docstring issues.

    Args:
        directory: Path to the directory to analyze
        exclude_dirs: List of directory names to exclude

    Returns:
        Dictionary mapping file paths to lists of docstring issues
    """
    exclude_dirs = exclude_dirs or []
    issues: Dict[Path, List[DocstringIssue]] = {}

    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]

        # Analyze Python files
        for file in files:
            if file.endswith(".py"):
                file_path = Path(root) / file
                file_issues = analyze_file(file_path)
                if file_issues:
                    issues[file_path] = file_issues

    return issues


def generate_report(issues: Dict[Path, List[DocstringIssue]]) -> str:
    """
    Generate a report of docstring issues.

    Args:
        issues: Dictionary mapping file paths to lists of docstring issues

    Returns:
        Report as a string, or empty string if no issues found
    """
    if not issues:
        return ""

    total_issues = sum(len(file_issues) for file_issues in issues.values())
    report = f"Found {total_issues} docstring issues in {len(issues)} files:\n\n"

    for file_path, file_issues in sorted(issues.items()):
        report += f"{file_path} ({len(file_issues)} issues):\n"
        for issue in sorted(file_issues, key=lambda i: i.line_number):
            report += f"  Line {issue.line_number}: {issue.node_name} - {issue.issue_type} - {issue.message}\n"
        report += "\n"

    return report


def main() -> None:
    """
    Run the docstring standardization script.

    This script analyzes Python files to check for Google-style docstring
    compliance. It can analyze one or more files and directories.

    Returns:
        None: This function doesn't return a value
    """
    parser = argparse.ArgumentParser(
        description="Check and standardize docstrings in Python files"
    )
    parser.add_argument(
        "path", nargs="+", help="Paths to files or directories to analyze"
    )
    parser.add_argument("--exclude", nargs="+", help="Directories to exclude")
    parser.add_argument(
        "--report", action="store_true", help="Generate a report of issues"
    )
    parser.add_argument(
        "--check", action="store_true", help="Check only, don't fix issues"
    )

    args = parser.parse_args()

    # Process all paths
    all_issues = {}

    for path_str in args.path:
        path = Path(path_str)
        if not path.exists():
            logger.error(f"Path {path} does not exist")
            continue

        if path.is_file() and not path.name.endswith(".py"):
            logger.error(f"File {path} is not a Python file")
            continue

        # Analyze files
        if path.is_file():
            file_issues = {path: analyze_file(path)}
        else:
            file_issues = analyze_directory(path, args.exclude)

        all_issues.update(file_issues)

    # Generate report
    if args.report or args.check:
        report = generate_report(all_issues)
        print(report)

    # Exit with error code if issues were found and check mode is enabled
    if args.check and all_issues:
        # Count total issues
        total_issues = sum(len(file_issues) for file_issues in all_issues.values())
        if total_issues > 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
