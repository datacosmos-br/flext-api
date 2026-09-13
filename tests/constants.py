"""Test constants for flext-api.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tests import FlextTestsConstants

from flext_api import c

if TYPE_CHECKING:
    from tests import t


class _ApiConstants:
    """API-specific test constants."""


class _WebConstants:
    """Web-specific test constants."""


class TestsFlextApiConstants(FlextTestsConstants, c):
    """Test constants for flext-api."""

    class TestsFlextApi(_ApiConstants, _WebConstants, FlextTestsConstants.Tests):
        """Test-specific constants."""


__all__: t.MutableSequenceOf[str] = ["TestsFlextApiConstants"]