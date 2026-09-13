"""Test protocols for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_api import p


class _ClientProtocols:
    """Client-specific test protocols."""


class _TransportProtocols:
    """Transport-specific test protocols."""


class TestsFlextApiProtocols(p):
    """Test protocols for flext-api — extends flext_api.p."""

    class TestsFlextApi(_ClientProtocols, _TransportProtocols):
        """Test-specific protocols."""


__all__: list[str] = ["TestsFlextApiProtocols"]