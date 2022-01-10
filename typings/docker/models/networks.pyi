"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

from docker.models.resource import Collection, Model

class Network(Model):
    @property
    def name(self): ...
    @property
    def containers(self): ...
    def connect(self, container, *args, **kwargs): ...
    def disconnect(self, container, *args, **kwargs): ...
    def remove(self): ...

class NetworkCollection(Collection):
    model = Network
    def create(self, name, *args, **kwargs): ...
    def get(self, network_id, *args, **kwargs): ...
    def list(self, *args, **kwargs): ...
    def prune(self, filters=...): ...