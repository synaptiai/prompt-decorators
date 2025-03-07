"""Configuration settings for prompt decorators package."""

from pathlib import Path
from typing import Any, Dict, Union

# Base paths
REPO_ROOT = Path(__file__).parent.parent
REGISTRY_PATH = REPO_ROOT / "registry"
OUTPUT_PATH = REPO_ROOT / "prompt_decorators" / "decorators"
TEST_PATH = REPO_ROOT / "tests"

# Registry paths
PATHS: Dict[str, Any] = {
    "registry": {
        "core": REGISTRY_PATH / "core",
        "extensions": REGISTRY_PATH / "extensions",
    },
    "output": {
        "code": {
            "core": OUTPUT_PATH / "core",
            "extensions": OUTPUT_PATH / "extensions",
        },
        "tests": {
            "core": TEST_PATH / "auto" / "core",
            "extensions": TEST_PATH / "auto" / "extensions",
        },
    },
    "templates": REPO_ROOT / "prompt_decorators" / "generator" / "templates",
}


# Function to ensure all required paths exist
def ensure_paths_exist() -> None:
    """Ensure all required paths exist."""
    output_paths = PATHS["output"]
    if isinstance(output_paths, dict):
        for path_category in output_paths.values():
            if isinstance(path_category, dict):
                for path in path_category.values():
                    if isinstance(path, Path):
                        path.mkdir(parents=True, exist_ok=True)

    test_paths = PATHS["output"].get("tests", {})
    if isinstance(test_paths, dict):
        for path in test_paths.values():
            if isinstance(path, Path):
                init_file = path / "__init__.py"
                if not init_file.exists():
                    init_file.touch()
