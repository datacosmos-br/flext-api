"""Generic HTTP client facade."""

from __future__ import annotations

from typing import override

from .. import p, r, t, u
from ._services import FlextApiClientRequestMixin
from .base_client import FlextApiClientBase


class FlextApiClient(FlextApiClientRequestMixin, FlextApiClientBase):
    """Generic HTTP client using FLEXT patterns."""

    @override
    def execute(self, **kwargs: t.Scalar) -> p.Result[bool]:
        """Execute service lifecycle parity."""
        if kwargs:
            u.fetch_logger(__name__).info(
                "Execute called with kwargs keys: %s", list(kwargs.keys())
            )
        return r[bool].ok(True)


__all__: t.MutableSequenceOf[str] = ["FlextApiClient"]
