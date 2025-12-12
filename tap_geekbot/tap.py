"""Geekbot tap class."""

from __future__ import annotations

from typing import override

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_geekbot.streams import Reports, StandUps, Teams


class TapGeekbot(Tap):
    """Singer tap for Geekbot."""

    name = "tap-geekbot"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API Key for Geekbot",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[Stream]:
        return [
            Teams(tap=self),
            Reports(tap=self),
            StandUps(tap=self),
        ]
