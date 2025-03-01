# Prompt Decorators Scripts

This directory contains utility scripts for the Prompt Decorators project.

## Available Scripts

### Release Script (`release.py`)

Automates the release process for the Prompt Decorators library.

**Features:**
- Updates version numbers in relevant files
- Updates the changelog with release details
- Creates a git tag
- Builds the distribution packages
- Uploads to PyPI (with optional confirmation)

**Usage:**
```bash
# Make the script executable (if not already)
chmod +x scripts/release.py

# Run the script
./scripts/release.py [--dry-run] [--no-confirm] [major|minor|patch]
```

**Arguments:**
- `major|minor|patch`: The part of the version to increment
- `--dry-run`: Run without making actual changes
- `--no-confirm`: Don't ask for confirmation before publishing to PyPI

**Example:**
```bash
# Increment the patch version (e.g., 0.1.0 -> 0.1.1)
./scripts/release.py patch

# Increment the minor version with a dry run (e.g., 0.1.0 -> 0.2.0)
./scripts/release.py --dry-run minor

# Increment the major version without confirmation (e.g., 0.1.0 -> 1.0.0)
./scripts/release.py --no-confirm major
```

## Adding New Scripts

When adding new scripts to this directory:

1. Make sure to add proper documentation in the script itself
2. Update this README with information about the script
3. Ensure the script is executable (`chmod +x scripts/your_script.py`)
4. Include proper error handling and logging
5. Add type annotations and follow the project's coding standards 