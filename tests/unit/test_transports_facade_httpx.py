"""The transport facade owns the httpx primitives consumers route through."""

from __future__ import annotations

import httpx

from flext_api import p


class TestsTransportsFacadeHttpx:
    """Httpx primitives surface identity and behavior through the owner."""

    def test_client_primitives_are_the_owner_types(self) -> None:
        """Client factories and response type are the httpx owner types."""
        assert p.Api.Transports.Httpx.Client is httpx.Client
        assert p.Api.Transports.Httpx.AsyncClient is httpx.AsyncClient
        assert p.Api.Transports.Httpx.Response is httpx.Response

    def test_exception_primitives_are_the_owner_types(self) -> None:
        """Exception types match the httpx owner for consumer except clauses."""
        assert p.Api.Transports.Httpx.HTTPError is httpx.HTTPError
        assert p.Api.Transports.Httpx.HTTPStatusError is httpx.HTTPStatusError
        assert p.Api.Transports.Httpx.RequestError is httpx.RequestError
        assert p.Api.Transports.Httpx.TimeoutException is httpx.TimeoutException

    def test_conflict_status_is_derived_from_the_owner(self) -> None:
        """The conflict constant stays int-typed and equals the httpx owner."""
        conflict = p.Api.Transports.Httpx.CONFLICT
        assert isinstance(conflict, int)
        assert conflict == int(httpx.codes.CONFLICT)

    def test_client_constructs_through_the_facade(self) -> None:
        """A real client constructs and closes through the facade alias."""
        client = p.Api.Transports.Httpx.Client(timeout=2.0)
        try:
            assert client.is_closed is False
        finally:
            client.close()
        assert client.is_closed is True
