"""Generic HTTP client facade."""

from __future__ import annotations

from typing import override

from .. import p, r, t, u
from ._services import FlextApiClientRequestMixin
from .base_client import FlextApiClientBase


class FlextApiClient(FlextApiClientRequestMixin, FlextApiClientBase):
    """Generic HTTP client using FLEXT patterns."""


__all__: t.MutableSequenceOf[str] = ["FlextApiClient"]
