"""Test utilities for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_api import u


class TestsFlextApiUtilities(u):
    """Test utilities for flext-api — extends flext_api.u."""
    
    class _RequestUtilities:
        """Request-specific test utilities."""
    
    class _ResponseUtilities:
        """Response-specific test utilities."""

    class TestsFlextApi(TestsFlextApiUtilities._RequestUtilities, TestsFlextApiUtilities._ResponseUtilities):
        """Test-specific utilities."""
__all__: list[str] = ["TestsFlextApiUtilities"]
