"""Test utilities for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_api import u


class _RequestUtilities:
    """Request-specific test utilities."""


class _ResponseUtilities:
    """Response-specific test utilities."""


class TestsFlextApiUtilities(FlextTestsUtilities, u):
    """Test utilities for flext-api."""

    class TestsFlextApi(_RequestUtilities, _ResponseUtilities, FlextTestsUtilities.Tests):
        """Test-specific utilities."""


__all__: list[str] = ["TestsFlextApiUtilities"]