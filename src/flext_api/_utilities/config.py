"""FlextApiUtilitiesConfig - declarative utilities constants (SSOT).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextApiUtilitiesConfig:
    """SSOT for API-specific utilities defaults."""

    UTILS_RETRY_DEFAULT: Final[int] = 3
    UTILS_TIMEOUT_DEFAULT: Final[int] = 30
