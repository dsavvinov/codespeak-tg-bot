"""Configuration utilities for the Telegram bot."""

import os
from pathlib import Path
from dotenv import dotenv_values


def _read_config_parameter(param_name: str) -> str | None:
    """
    Read a configuration parameter from the .env.local file without mutating the current environment.
    Note that it's important that the function reads the parameter from the .env.local file first,
    and then from the environment variables.
    Case-insensitive.
    """
    param_name = param_name.upper()
    file = Path(".env.local")
    env_map = dotenv_values(file) if file.exists() else {}
    value_from_env_local = env_map.get(param_name)
    value_from_env = os.getenv(param_name)
    return value_from_env_local or value_from_env or None


def get_telegram_bot_token() -> str:
    """Get the Telegram bot token from configuration."""
    token = _read_config_parameter("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN is required. Please set it in .env.local or as an environment variable."
        )
    return token