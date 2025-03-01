#!/usr/bin/env python3
"""
Prompt Decorators Release Script

This script automates the release process for the Prompt Decorators library:
1. Updates version numbers in relevant files
2. Updates the changelog with release details
3. Creates a git tag
4. Builds the distribution packages
5. Uploads to PyPI (with optional confirmation)

Usage:
    python scripts/release.py [--dry-run] [--no-confirm] [major|minor|patch]

Arguments:
    major|minor|patch: The part of the version to increment
    --dry-run: Run without making actual changes
    --no-confirm: Don't ask for confirmation before publishing to PyPI
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Optional, Tuple


class VersionPart(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


class ReleaseManager:
    """Manages the release process for the Prompt Decorators library."""

    def __init__(self, dry_run: bool = False, confirm: bool = True):
        """Initialize the release manager.
        
        Args:
            dry_run: If True, don't make actual changes
            confirm: If True, ask for confirmation before publishing to PyPI
        """
        self.dry_run = dry_run
        self.confirm = confirm
        self.root_dir = Path(__file__).parent.parent
        self.version_pattern = re.compile(r'(\d+)\.(\d+)\.(\d+)')
        
    def run(self, version_part: VersionPart) -> None:
        """Run the release process.
        
        Args:
            version_part: Which part of the version to increment
        """
        # Get the current version
        current_version = self._get_current_version()
        if not current_version:
            print("Error: Could not determine current version")
            sys.exit(1)
        
        # Calculate the new version
        new_version = self._increment_version(current_version, version_part)
        
        print(f"Current version: {'.'.join(map(str, current_version))}")
        print(f"New version: {'.'.join(map(str, new_version))}")
        
        if self.dry_run:
            print("\nDRY RUN: No changes will be made")
            return

        # Update version in files
        self._update_version_in_files(current_version, new_version)
        
        # Update the changelog
        self._update_changelog(new_version)
        
        # Commit and tag
        self._commit_and_tag(new_version)
        
        # Build and publish
        self._build_and_publish()
        
        print(f"\nRelease {'.'.join(map(str, new_version))} completed successfully!")
        
    def _get_current_version(self) -> Optional[Tuple[int, int, int]]:
        """Get the current version from __init__.py.
        
        Returns:
            Tuple of (major, minor, patch) or None if not found
        """
        init_file = self.root_dir / "prompt_decorators" / "__init__.py"
        if not init_file.exists():
            print(f"Error: Could not find {init_file}")
            return None
            
        with open(init_file, "r") as f:
            content = f.read()
            
        match = self.version_pattern.search(content)
        if not match:
            print(f"Error: Could not find version in {init_file}")
            return None
            
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        
    def _increment_version(
        self, version: Tuple[int, int, int], part: VersionPart
    ) -> Tuple[int, int, int]:
        """Increment the version according to semver.
        
        Args:
            version: Current version as (major, minor, patch)
            part: Which part to increment
        
        Returns:
            New version as (major, minor, patch)
        """
        major, minor, patch = version
        
        if part == VersionPart.MAJOR:
            return (major + 1, 0, 0)
        elif part == VersionPart.MINOR:
            return (major, minor + 1, 0)
        else:  # PATCH
            return (major, minor, patch + 1)
    
    def _update_version_in_files(
        self, current_version: Tuple[int, int, int], new_version: Tuple[int, int, int]
    ) -> None:
        """Update version numbers in all relevant files.
        
        Args:
            current_version: Current version as (major, minor, patch)
            new_version: New version as (major, minor, patch)
        """
        current_version_str = '.'.join(map(str, current_version))
        new_version_str = '.'.join(map(str, new_version))
        
        # Files to update
        files_to_update = [
            self.root_dir / "prompt_decorators" / "__init__.py",
            self.root_dir / "pyproject.toml",
            self.root_dir / "setup.py"
        ]
        
        for file_path in files_to_update:
            if not file_path.exists():
                print(f"Warning: Could not find {file_path}")
                continue
                
            with open(file_path, "r") as f:
                content = f.read()
                
            if current_version_str not in content:
                print(f"Warning: Could not find version {current_version_str} in {file_path}")
                continue
                
            new_content = content.replace(current_version_str, new_version_str)
            
            with open(file_path, "w") as f:
                f.write(new_content)
                
            print(f"Updated version in {file_path}")
            
    def _update_changelog(self, new_version: Tuple[int, int, int]) -> None:
        """Update the CHANGELOG.md file.
        
        Args:
            new_version: New version as (major, minor, patch)
        """
        changelog_path = self.root_dir / "CHANGELOG.md"
        if not changelog_path.exists():
            print("Warning: Could not find CHANGELOG.md")
            return
            
        with open(changelog_path, "r") as f:
            lines = f.readlines()
            
        # Find the "Unreleased" section
        unreleased_index = -1
        for i, line in enumerate(lines):
            if "## [Unreleased]" in line:
                unreleased_index = i
                break
                
        if unreleased_index == -1:
            print("Warning: Could not find '## [Unreleased]' section in CHANGELOG.md")
            return
            
        # Find the next ## section
        next_section_index = -1
        for i in range(unreleased_index + 1, len(lines)):
            if lines[i].startswith('## ['):
                next_section_index = i
                break
                
        if next_section_index == -1:
            print("Warning: Could not find next section after 'Unreleased'")
            return
            
        # Extract the unreleased content
        unreleased_content = lines[unreleased_index + 1:next_section_index]
        
        # Create the new release section
        today = datetime.now().strftime("%Y-%m-%d")
        new_version_str = '.'.join(map(str, new_version))
        new_section = [f"\n## [{new_version_str}] - {today}\n"] + unreleased_content
        
        # Create a new unreleased section
        new_unreleased = [
            "## [Unreleased]\n",
            "\n",
            "### Added\n",
            "\n",
            "### Changed\n",
            "\n",
            "### Fixed\n",
            "\n"
        ]
        
        # Create the updated changelog
        updated_lines = (
            lines[:unreleased_index] + 
            new_unreleased + 
            new_section + 
            lines[next_section_index:]
        )
        
        with open(changelog_path, "w") as f:
            f.writelines(updated_lines)
            
        print(f"Updated CHANGELOG.md with {new_version_str} release")
    
    def _commit_and_tag(self, new_version: Tuple[int, int, int]) -> None:
        """Commit changes and create a git tag.
        
        Args:
            new_version: New version as (major, minor, patch)
        """
        new_version_str = '.'.join(map(str, new_version))
        
        # Get modified files
        result = self._run_command(["git", "status", "--porcelain"])
        modified_files = [line[3:] for line in result.strip().split('\n') if line]
        
        if not modified_files:
            print("Warning: No modified files to commit")
            return
            
        # Commit changes
        self._run_command(["git", "add"] + modified_files)
        self._run_command([
            "git", "commit", "-m", f"Release version {new_version_str}"
        ])
        
        # Create tag
        self._run_command([
            "git", "tag", "-a", f"v{new_version_str}", "-m", f"Version {new_version_str}"
        ])
        
        print(f"Committed changes and created tag v{new_version_str}")
    
    def _build_and_publish(self) -> None:
        """Build and publish the package to PyPI."""
        # Clean up any previous builds
        dist_dir = self.root_dir / "dist"
        if dist_dir.exists():
            self._run_command(["rm", "-rf", str(dist_dir)])
            
        # Build the package
        self._run_command(["python", "-m", "build"])
        
        # Publish to PyPI if confirmed
        if not self.confirm or self._confirm_publish():
            self._run_command(["python", "-m", "twine", "upload", "dist/*"])
            print("Package published to PyPI")
        else:
            print("Publishing to PyPI skipped")
    
    def _confirm_publish(self) -> bool:
        """Ask for confirmation before publishing to PyPI.
        
        Returns:
            True if confirmed, False otherwise
        """
        response = input("\nDo you want to publish to PyPI? (y/N): ").lower()
        return response in ("y", "yes")
    
    def _run_command(self, command: List[str]) -> str:
        """Run a shell command and return its output.
        
        Args:
            command: Command to run as a list of strings
            
        Returns:
            Command output
            
        Raises:
            SystemExit: If the command fails
        """
        print(f"Running: {' '.join(command)}")
        
        try:
            result = subprocess.run(
                command, 
                check=True, 
                text=True, 
                capture_output=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: Command failed with exit code {e.returncode}")
            print(f"Error output: {e.stderr}")
            sys.exit(1)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.
    
    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Prompt Decorators release script")
    parser.add_argument(
        "version_part",
        choices=["major", "minor", "patch"],
        help="Part of the version to increment"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without making actual changes"
    )
    parser.add_argument(
        "--no-confirm",
        action="store_true",
        help="Don't ask for confirmation before publishing to PyPI"
    )
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    
    version_part = VersionPart(args.version_part)
    release_manager = ReleaseManager(
        dry_run=args.dry_run,
        confirm=not args.no_confirm
    )
    
    release_manager.run(version_part) 