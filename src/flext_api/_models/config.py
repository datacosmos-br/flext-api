"""FlextApiModelsConfig - declarative model constants (SSOT).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextApiModelsConfig:
    """SSOT for API-specific model defaults."""

    MODEL_CONFIG_FROZEN: Final[bool] = True
    MODEL_CONFIG_STR_STRIP_WHITESPACE: Final[bool] = True
