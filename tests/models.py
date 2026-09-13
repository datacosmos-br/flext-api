"""Test models for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_api import m


class _RequestModels:
    """Request-specific test models."""


class _ResponseModels:
    """Response-specific test models."""


class TestsFlextApiModels(FlextTestsModels, m):
    """Test models for flext-api."""

    class TestsFlextApi(_RequestModels, _ResponseModels, FlextTestsModels.Tests):
        """Test-specific models."""


__all__: list[str] = ["TestsFlextApiModels"]