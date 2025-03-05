"""
Configuration management for the OpenAI prompt decorator demo.

This module provides utilities for loading and managing configuration
from environment variables and config files.
"""

import json
import os
from typing import Any, Dict

from dotenv import load_dotenv


def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables and config files.

    Returns:
        Dict[str, Any]: Configuration dictionary with all settings
    """
    load_dotenv()

    config = {
        "openai": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "default_model": os.getenv("OPENAI_MODEL", "gpt-4o"),
            "temperature": float(os.getenv("OPENAI_TEMPERATURE", "0.7")),
        },
        "decorators": {
            "enabled": True,
            "log_decorated_prompts": True,
        },
    }

    # Load from config file if it exists
    config_path = os.getenv("CONFIG_PATH", "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            file_config = json.load(f)
            # Merge configs
            for section, values in file_config.items():
                if section in config:
                    if isinstance(config[section], dict) and isinstance(values, dict):
                        # Use type casting to help mypy understand this is a dict
                        section_dict = config[section]
                        section_dict.update(values)  # type: ignore
                    else:
                        config[section] = values
                else:
                    config[section] = values

    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate the configuration to ensure all required fields are present.

    Args:
        config: The configuration dictionary to validate

    Returns:
        bool: True if configuration is valid, False otherwise
    """
    # Check if OpenAI API key is present
    if not config.get("openai", {}).get("api_key"):
        print(
            "ERROR: OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable."
        )
        return False

    return True


def load_config_value(env_var: str, config_key: str, default: Any = None) -> Any:
    """
    Load a configuration value from environment variables or the config dictionary.

    Args:
        env_var: Environment variable name to check first
        config_key: Key in the configuration dictionary to check next
        default: Default value to return if neither source has the value

    Returns:
        Any: The configuration value from environment, config, or default
    """
    # Check environment first
    env_value = os.getenv(env_var)
    if env_value is not None:
        return env_value

    # Load config and check for the key
    config = load_config()

    # The key might be nested (e.g., "openai.api_key")
    if "." in config_key:
        parts = config_key.split(".")
        value = config
        for part in parts:
            if part in value:
                value = value[part]
            else:
                return default
        return value

    # Simple key lookup
    if config_key in config:
        return config[config_key]

    # Return default if not found
    return default
