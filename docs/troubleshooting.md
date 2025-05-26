# Troubleshooting Guide

This guide helps you diagnose and resolve common issues with the Prompt Decorators framework.

## Quick Diagnosis

If you're experiencing issues, start with these quick diagnostic commands:

```bash
# Check package installation
python -c "import prompt_decorators; print(f'Version: {prompt_decorators.__version__}')"

# Verify registry loading
python -m prompt_decorators verify

# Check available decorators
python -c "from prompt_decorators import get_available_decorators; print(f'Loaded decorators: {len(get_available_decorators())}')"
```

## Common Issues

### Registry Loading Problems

#### Issue: "No decorators loaded" or "Registry is empty"

**Symptoms:**
- `get_available_decorators()` returns an empty list
- Error messages about missing decorators
- Registry verification fails

**Causes:**
- Package installed without registry files
- Registry directories are empty or missing
- Installation was incomplete

**Solutions:**

1. **Auto-Repair (Recommended)**:
   ```bash
   python -m prompt_decorators repair
   ```

2. **Manual Verification**:
   ```bash
   python -m prompt_decorators verify
   ```

3. **Check Registry Directories**:
   ```python
   import prompt_decorators
   from pathlib import Path

   # Check registry path
   registry_path = Path(prompt_decorators.__file__).parent / "registry"
   print(f"Registry path: {registry_path}")
   print(f"Registry exists: {registry_path.exists()}")

   # List registry contents
   if registry_path.exists():
       json_files = list(registry_path.rglob("*.json"))
       print(f"Found {len(json_files)} JSON files")
       for file in json_files[:5]:  # Show first 5
           print(f"  {file}")
   ```

4. **Reinstall Package**:
   ```bash
   pip uninstall prompt-decorators
   pip install --no-cache-dir prompt-decorators
   python -m prompt_decorators verify
   ```

#### Issue: "Registry verification failed"

**Symptoms:**
- Verification command reports failures
- Some decorators missing or corrupted

**Solutions:**

1. **Force Repair**:
   ```bash
   python -m prompt_decorators repair --force
   ```

2. **Check Specific Directories**:
   ```python
   from pathlib import Path
   import prompt_decorators

   registry_path = Path(prompt_decorators.__file__).parent / "registry"

   # Check each subdirectory
   for subdir in ["core", "extensions", "simplified_decorators"]:
       path = registry_path / subdir
       if path.exists():
           files = list(path.rglob("*.json"))
           print(f"{subdir}: {len(files)} files")
       else:
           print(f"{subdir}: MISSING")
   ```

### Decorator Application Issues

#### Issue: "Decorator not found" errors

**Symptoms:**
- `DecoratorNotFoundError` when using decorators
- Specific decorators not available

**Solutions:**

1. **Check Decorator Name**:
   ```python
   from prompt_decorators import get_available_decorators

   # List all available decorators
   decorators = get_available_decorators()
   decorator_names = [d.name for d in decorators]
   print("Available decorators:")
   for name in sorted(decorator_names):
       print(f"  {name}")
   ```

2. **Verify Case Sensitivity**:
   ```python
   # Decorator names are case-sensitive
   # ✓ Correct: "StepByStep"
   # ✗ Wrong: "stepbystep", "STEPBYSTEP"
   ```

3. **Check for Typos**:
   ```python
   from difflib import get_close_matches

   decorator_names = [d.name for d in get_available_decorators()]
   attempted_name = "StepByStap"  # Example typo

   matches = get_close_matches(attempted_name, decorator_names, n=3)
   print(f"Did you mean: {matches}")
   ```

#### Issue: Decorator syntax errors

**Symptoms:**
- Decorators not being parsed correctly
- Unexpected behavior in decorator application

**Solutions:**

1. **Verify Syntax**:
   ```python
   # ✓ Correct syntax
   prompt = """
   +++StepByStep(numbered=true)
   +++Audience(level="beginner")
   Explain quantum computing.
   """

   # ✗ Common mistakes
   # Missing +++: "StepByStep(numbered=true)"
   # Wrong quotes: "+++StepByStep(numbered='true')"
   # Missing parameters: "+++StepByStep()"
   ```

2. **Test Decorator Parsing**:
   ```python
   from prompt_decorators.core.parser import extract_decorators

   prompt = "+++StepByStep(numbered=true)\nExplain something."
   decorators = extract_decorators(prompt)
   print(f"Parsed decorators: {decorators}")
   ```

### Installation Issues

#### Issue: Package not found during installation

**Symptoms:**
- `pip install prompt-decorators` fails
- "No matching distribution found" errors

**Solutions:**

1. **Check Package Name**:
   ```bash
   # ✓ Correct
   pip install prompt-decorators

   # ✗ Wrong
   pip install prompt_decorators
   pip install promptdecorators
   ```

2. **Update pip**:
   ```bash
   python -m pip install --upgrade pip
   pip install prompt-decorators
   ```

3. **Check Python Version**:
   ```bash
   python --version  # Should be 3.11+
   ```

#### Issue: Permission errors during installation

**Solutions:**

1. **Use User Installation**:
   ```bash
   pip install --user prompt-decorators
   ```

2. **Use Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install prompt-decorators
   ```

### Development Issues

#### Issue: Tests failing in development environment

**Solutions:**

1. **Verify Development Setup**:
   ```bash
   # Install development dependencies
   pip install -e ".[dev,test,docs]"

   # Run registry preparation
   python scripts/prepare_build.py

   # Verify setup
   python -m prompt_decorators verify
   ```

2. **Run Specific Tests**:
   ```bash
   # Run registry tests
   pytest tests/ -k "registry" -v

   # Run with coverage
   pytest --cov=prompt_decorators tests/
   ```

#### Issue: Build failures

**Solutions:**

1. **Prepare Build Environment**:
   ```bash
   # Clean previous builds
   rm -rf dist/ build/ *.egg-info/

   # Prepare registry files
   python scripts/prepare_build.py

   # Verify build contents
   python scripts/verify_build.py

   # Build package
   poetry build
   ```

2. **Check MANIFEST.in**:
   ```bash
   # Verify MANIFEST.in includes registry files
   python setup.py check --restructuredtext --strict
   ```

## Advanced Diagnostics

### Registry System Deep Dive

```python
import json
from pathlib import Path
import prompt_decorators
from prompt_decorators.core.dynamic_decorator import DynamicDecorator

# Get registry path
registry_path = Path(prompt_decorators.__file__).parent / "registry"

# Check registry structure
def check_registry_structure():
    print(f"Registry path: {registry_path}")
    print(f"Exists: {registry_path.exists()}")

    if not registry_path.exists():
        print("❌ Registry directory missing")
        return False

    # Check subdirectories
    subdirs = ["core", "extensions", "simplified_decorators"]
    for subdir in subdirs:
        path = registry_path / subdir
        if path.exists():
            json_files = list(path.rglob("*.json"))
            print(f"✅ {subdir}: {len(json_files)} files")
        else:
            print(f"❌ {subdir}: missing")

    return True

# Test decorator loading
def test_decorator_loading():
    try:
        decorator = DynamicDecorator()
        decorator.load_registry()
        count = len(decorator._registry)
        print(f"✅ Loaded {count} decorators")
        return True
    except Exception as e:
        print(f"❌ Loading failed: {e}")
        return False

# Run diagnostics
check_registry_structure()
test_decorator_loading()
```

### Performance Diagnostics

```python
import time
from prompt_decorators import apply_dynamic_decorators

# Test performance
def test_performance():
    prompt = """
    +++StepByStep(numbered=true)
    +++Reasoning(depth="comprehensive")
    +++Audience(level="intermediate")
    Explain how neural networks work.
    """

    start_time = time.time()
    result = apply_dynamic_decorators(prompt)
    end_time = time.time()

    print(f"Processing time: {end_time - start_time:.4f} seconds")
    print(f"Input length: {len(prompt)} characters")
    print(f"Output length: {len(result)} characters")

test_performance()
```

## Getting Help

If you're still experiencing issues after trying these solutions:

1. **Check the FAQ**: [docs/faq.md](faq.md)
2. **Search existing issues**: [GitHub Issues](https://github.com/synaptiai/prompt-decorators/issues)
3. **Create a new issue**: Include:
   - Output of `python -m prompt_decorators verify`
   - Your Python version (`python --version`)
   - Your operating system
   - Steps to reproduce the issue
   - Full error messages

## Preventive Measures

### Regular Maintenance

```bash
# Verify installation periodically
python -m prompt_decorators verify

# Update to latest version
pip install --upgrade prompt-decorators

# Clear cache if needed
pip cache purge
```

### Development Best Practices

1. **Always verify registry after setup**:
   ```bash
   python scripts/prepare_build.py
   python -m prompt_decorators verify
   ```

2. **Use virtual environments**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Keep dependencies updated**:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

## Emergency Recovery

If your installation is completely broken:

```bash
# Nuclear option: complete reinstall
pip uninstall prompt-decorators
pip cache purge
pip install --no-cache-dir --force-reinstall prompt-decorators

# Verify recovery
python -m prompt_decorators verify
```

This should resolve most installation and registry issues.
