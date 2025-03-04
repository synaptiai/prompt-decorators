#!/usr/bin/env python
"""Fix Common Issues Script.

This script fixes common issues that cause pre-commit hooks to fail, such as:
- Trailing whitespace
- Missing newline at end of file
- Mixed line endings

Usage:
    python scripts/fix_common_issues.py [--all]

Options:
    --all: Fix all files in the repository (default: only staged files)
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd):
    """Run a command and return its output."""
    process = subprocess.run(cmd, capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr


def get_files_to_fix(all_files=False):
    """Get the list of files to fix."""
    if all_files:
        # Get all tracked files
        returncode, stdout, stderr = run_command(["git", "ls-files"])
        if returncode != 0:
            print(f"Error getting tracked files: {stderr}")
            return []
        return stdout.splitlines()
    else:
        # Get staged files
        returncode, stdout, stderr = run_command(
            ["git", "diff", "--cached", "--name-only"]
        )
        if returncode != 0:
            print(f"Error getting staged files: {stderr}")
            return []
        return stdout.splitlines()


def is_binary_file(file_path):
    """Check if a file is binary."""
    # Common binary file extensions
    binary_extensions = {
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".ico",
        ".tif",
        ".tiff",
        ".pdf",
        ".doc",
        ".docx",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx",
        ".zip",
        ".tar",
        ".gz",
        ".bz2",
        ".7z",
        ".rar",
        ".exe",
        ".dll",
        ".so",
        ".dylib",
        ".pyc",
        ".pyo",
        ".pyd",
        ".mp3",
        ".mp4",
        ".avi",
        ".mov",
        ".flv",
        ".wav",
    }

    # Check extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext in binary_extensions:
        return True

    # Try to read as text
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read(1024)
        return False
    except UnicodeDecodeError:
        return True


def fix_trailing_whitespace(file_path):
    """Fix trailing whitespace in a file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        fixed = False
        for i, line in enumerate(lines):
            stripped = line.rstrip()
            if stripped != line.rstrip("\n"):
                lines[i] = stripped + (
                    line[len(line.rstrip()) :] if line.endswith("\n") else ""
                )
                fixed = True

        if fixed:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"Fixed trailing whitespace in {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error fixing trailing whitespace in {file_path}: {e}")
        return False


def fix_end_of_file(file_path):
    """Ensure file ends with a newline."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if not content.endswith("\n"):
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n")
            print(f"Fixed end of file in {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error fixing end of file in {file_path}: {e}")
        return False


def fix_mixed_line_endings(file_path):
    """Fix mixed line endings in a file."""
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        if b"\r\n" in content and b"\n" in content.replace(b"\r\n", b""):
            # Convert to LF
            content = content.replace(b"\r\n", b"\n")
            with open(file_path, "wb") as f:
                f.write(content)
            print(f"Fixed mixed line endings in {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error fixing mixed line endings in {file_path}: {e}")
        return False


def main():
    """Run the script."""
    parser = argparse.ArgumentParser(
        description="Fix common issues that cause pre-commit hooks to fail"
    )
    parser.add_argument(
        "--all", action="store_true", help="Fix all files in the repository"
    )
    args = parser.parse_args()

    files = get_files_to_fix(args.all)
    if not files:
        print("No files to fix")
        return

    fixed_files = set()
    skipped_files = set()

    for file_path in files:
        if not os.path.exists(file_path):
            continue

        # Skip binary files
        if is_binary_file(file_path):
            skipped_files.add(file_path)
            continue

        # Apply fixes
        if fix_trailing_whitespace(file_path):
            fixed_files.add(file_path)
        if fix_end_of_file(file_path):
            fixed_files.add(file_path)
        if fix_mixed_line_endings(file_path):
            fixed_files.add(file_path)

    if fixed_files:
        print(f"\nFixed {len(fixed_files)} files:")
        for file_path in sorted(fixed_files):
            print(f"  - {file_path}")
    else:
        print("\nNo issues found")

    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} binary files")


if __name__ == "__main__":
    main()
