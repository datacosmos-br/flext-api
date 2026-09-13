"""FlextApi utilities facade."""

from __future__ import annotations

from flext_web import u

from . import t
from ._utilities import (
    FlextApiUtilitiesApiPydantic,
    FlextApiUtilitiesRequestUtils,
    FlextApiUtilitiesSerializers,
    FlextApiUtilitiesSettingsManager,
)
from ._utilities.base import FlextApiUtilitiesBase
from ._utilities.config import FlextApiUtilitiesConfig


class FlextApiUtilities(u):
    """FlextApi utilities extending FlextUtilities with API-specific helpers."""

    class Api(
        FlextApiUtilitiesBase,
        FlextApiUtilitiesConfig,
        FlextApiUtilitiesApiPydantic,
        FlextApiUtilitiesRequestUtils,
        FlextApiUtilitiesSerializers,
        FlextApiUtilitiesSettingsManager,
    ):
        """API-specific utility namespace."""


__all__: t.MutableSequenceOf[str] = ["FlextApiUtilities", "u"]

u = FlextApiUtilities
