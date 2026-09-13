"""Test protocols for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_api import p


class _ClientProtocols:
    """Client-specific test protocols."""


class _TransportProtocols:
    """Transport-specific test protocols."""


class TestsFlextApiProtocols(FlextTestsProtocols, p):
    """Test protocols for flext-api."""

    class TestsFlextApi(_ClientProtocols, _TransportProtocols, FlextTestsProtocols.Tests):
        """Test-specific protocols."""


__all__: list[str] = ["TestsFlextApiProtocols"]