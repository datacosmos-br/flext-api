"""Generic protocol definitions for HTTP operations.

All protocol interfaces are centralized here following FLEXT standards.
Single unified class with nested protocol definitions organized under .Api namespace.
Domain-agnostic and reusable across any HTTP implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import httpx
from flext_web import p

from ._protocols import (
    FlextApiProtocolPlugins,
    FlextApiProtocolsBase,
    FlextApiProtocolsSerialization,
    FlextApiProtocolsTransports,
)


class FlextApiProtocols(p):
    """Single unified HTTP protocols class extending flext-core FlextProtocols."""

    class Api(
        FlextApiProtocolsBase,
        FlextApiProtocolPlugins,
        FlextApiProtocolsSerialization,
        FlextApiProtocolsTransports,
    ):
        """API-specific protocol namespace.

        All API domain-specific protocols are organized here to enable
        proper namespace separation. Parent protocols from flext-core are
        accessible via parent class (e.g., `p.Result`).
        """


p = FlextApiProtocols

# Module-level explicit aliases: valid per PEP 613, real classes at runtime,
# so consumer isinstance narrowing keeps both its static and runtime meaning.
type HttpxClient = httpx.Client
type HttpxAsyncClient = httpx.AsyncClient
type HttpxResponse = httpx.Response
type HttpxHTTPError = httpx.HTTPError
type HttpxHTTPStatusError = httpx.HTTPStatusError
type HttpxRequestError = httpx.RequestError
type HttpxTimeoutException = httpx.TimeoutException

__all__: list[str] = [
    "FlextApiProtocols",
    "FlextApiProtocolsTransports",
    "HttpxAsyncClient",
    "HttpxClient",
    "HttpxHTTPError",
    "HttpxHTTPStatusError",
    "HttpxRequestError",
    "HttpxResponse",
    "HttpxTimeoutException",
    "p",
]
