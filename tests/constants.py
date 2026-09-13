"""Test constants for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_api import c

if TYPE_CHECKING:
    from tests import t


class _ApiConstants:
    """API-specific test constants."""


class _WebConstants:
    """Web-specific test constants."""


class TestsFlextApiConstants(c):
    """Test constants for flext-api — extends flext_api.c."""

    class TestsFlextApi(_ApiConstants, _WebConstants):
        """Test-specific constants."""


__all__: list[str] = ["TestsFlextApiConstants"]