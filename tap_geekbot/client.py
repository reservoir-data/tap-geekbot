"""REST client handling, including GeekbotStream base class."""

from __future__ import annotations

from typing import override

from singer_sdk import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator


class GeekbotStream(RESTStream):
    """Geekbot stream class."""

    url_base = "https://api.geekbot.com"
    records_jsonpath = "$[*]"
    primary_keys = ("id",)

    @property
    @override
    def authenticator(self) -> APIKeyAuthenticator:
        return APIKeyAuthenticator(
            key="Authorization",
            value=self.config["api_key"],
            location="header",
        )
