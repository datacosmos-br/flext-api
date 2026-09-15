"""Generic async HTTP client facade."""

from __future__ import annotations

from typing import override

from .. import p, r, t, u
from ._services import FlextApiClientAsyncRequestMixin
from .base_client import FlextApiClientBase


class FlextApiAsyncClient(FlextApiClientAsyncRequestMixin, FlextApiClientBase):
    """Generic async HTTP client using FLEXT patterns."""


__all__: t.MutableSequenceOf[str] = ["FlextApiAsyncClient"]
