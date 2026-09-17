"""Test models for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_api import m


class TestsFlextApiModels(m):
    """Test models for flext-api — extends flext_api.m."""
    
    class _RequestModels:
        """Request-specific test models."""
    
    class _ResponseModels:
        """Response-specific test models."""

    class TestsFlextApi(_RequestModels, _ResponseModels):
        """Test-specific models."""
__all__: list[str] = ["TestsFlextApiModels"]
