"""FlextApiConstantsConfig - declarative config loading constants (SSOT).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextApiConstantsConfig:
    """SSOT for API-specific config loading defaults."""

    CONFIG_DIR_NAME: Final[str] = "config"
    CONFIG_SCHEMAS_DIR_NAME: Final[str] = "schemas"
    CONFIG_TEMPLATES_DIR_NAME: Final[str] = "templates"
    CONFIG_SETTINGS_FILE_NAME: Final[str] = "settings.yaml"
    CONFIG_SCHEMA_SUFFIX: Final[str] = ".schema.json"
    CONFIG_DEFAULT_ENCODING: Final[str] = "utf-8"
    CONFIG_TOML_SUFFIX: Final[str] = ".toml"
    CONFIG_YAML_SUFFIX: Final[str] = ".yaml"
    CONFIG_JSON_SUFFIX: Final[str] = ".json"
    CONFIG_EXPAND_MAX_PASSES: Final[int] = 10
