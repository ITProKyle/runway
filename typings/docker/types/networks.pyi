"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

class EndpointConfig(dict):
    def __init__(
        self,
        version,
        aliases=...,
        links=...,
        ipv4_address=...,
        ipv6_address=...,
        link_local_ips=...,
        driver_opt=...,
    ) -> None: ...

class NetworkingConfig(dict):
    def __init__(self, endpoints_config=...) -> None: ...

class IPAMConfig(dict):
    def __init__(self, driver=..., pool_configs=..., options=...) -> None: ...

class IPAMPool(dict):
    def __init__(
        self, subnet=..., iprange=..., gateway=..., aux_addresses=...
    ) -> None: ...