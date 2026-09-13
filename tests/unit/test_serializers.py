"""Behavioral tests for flext_api serialization utilities.

Exercises the PUBLIC contract of ``u.Api.packb`` / ``u.Api.unpackb`` only:
observable return values, the ``r[t.JsonValue]`` outcome of the fallible
``unpackb`` operation, round-trip idempotence, and error propagation. No
implementation internals are inspected.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_api import Api, t
from tests import u


class TestsFlextApiSerializers:
    """Public-contract behavior of packb/unpackb."""

    # ---- unpackb success --------------------------------------------------

    @pytest.mark.parametrize(
        ("packed", "expected"),
        [
            (b"\x81\xa3key\xa5value", {"key": "value"}),
            (b"\x93\x01\x02\x03", [1, 2, 3]),
            (b"\x2a", 42),
        ],
    )
    def test_unpackb_valid_input_succeeds(
        self, packed: bytes, expected: t.JsonValue
    ) -> None:
        """Valid msgpack decodes to its JSON value inside a successful result."""
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.failure, eq=False)
        tm.that(result.value, eq=expected)
        tm.that(result.error, none=True)

    def test_unpackb_success_unwraps_to_value(self) -> None:
        """unwrap() on a success yields the decoded value directly."""
        result = Api.unpackb(b"\x81\xa3key\xa5value")

        tm.that(result.unwrap(), eq={"key": "value"})

    def test_unpackb_success_supports_map_combinator(self) -> None:
        """A successful result composes through map() over its value."""
        result = Api.unpackb(b"\x81\xa3key\xa5value").map(lambda value: [value])

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=[{"key": "value"}])

    def test_unpackb_success_supports_flat_map_combinator(self) -> None:
        """A successful result chains a further fallible step via flat_map()."""
        result = Api.unpackb(b"\x2a").flat_map(
            lambda value: Api.unpackb(Api.packb(value))
        )

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=42)

    def test_unpackb_invalid_input_fails(self) -> None:
        """Invalid msgpack yields a failure with an error message."""
        result = Api.unpackb(b"\xff")

        tm.that(result.success, eq=False)
        tm.that(result.failure, eq=True)
        tm.that(result.error, is_str=True)

    def test_packb_unpackb_roundtrip(self) -> None:
        """packb() followed by unpackb() yields the original value."""
        original: t.JsonValue = {"key": "value", "list": [1, 2, 3]}
        packed = Api.packb(original)
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=original)

    def test_packb_valid_input_succeeds(self) -> None:
        """Valid JSON values pack successfully."""
        result = Api.packb({"key": "value"})

        tm.that(result.success, eq=True)
        tm.that(isinstance(result.value, bytes), eq=True)

    def test_packb_unpackb_roundtrip_list(self) -> None:
        """Round-trip for lists."""
        original: t.JsonValue = [1, 2, 3]
        packed = Api.packb(original)
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=original)

    def test_packb_unpackb_roundtrip_str(self) -> None:
        """Round-trip for strings."""
        original = "hello world"
        packed = Api.packb(original)
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=original)

    def test_packb_unpackb_roundtrip_bool(self) -> None:
        """Round-trip for booleans."""
        original = True
        packed = Api.packb(original)
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=original)

    def test_packb_unpackb_roundtrip_none(self) -> None:
        """Round-trip for null."""
        original = None
        packed = Api.packb(original)
        result = Api.unpackb(packed)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=original)


__all__: list[str] = ["TestsFlextApiSerializers"]

