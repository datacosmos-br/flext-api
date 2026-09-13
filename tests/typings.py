"""Test type aliases for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_api import t


class _RequestTypes:
    """Request-specific test type aliases."""


class _ResponseTypes:
    """Response-specific test type aliases."""


class TestsFlextApiTypes(FlextTestsTypes, t):
    """Test type aliases for flext-api."""

    class TestsFlextApi(_RequestTypes, _ResponseTypes, FlextTestsTypes.Tests):
        """Test-specific type aliases."""


__all__: list[str] = ["TestsFlextApiTypes"]