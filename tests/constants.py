"""Test constants for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_api import c


class TestsFlextApiConstants(c):
    """Test constants for flext-api — extends flext_api.c."""
    
    class _ApiConstants:
        """API-specific test constants."""
    
    class _WebConstants:
        """Web-specific test constants."""

    class TestsFlextApi(TestsFlextApiConstants._ApiConstants, TestsFlextApiConstants._WebConstants):
        """Test-specific constants."""
__all__: list[str] = ["TestsFlextApiConstants"]
