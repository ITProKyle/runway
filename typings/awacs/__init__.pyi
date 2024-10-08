"""This type stub file was generated by pyright."""

from __future__ import annotations

import json
import re
from typing import Any

__version__ = "1.0.1"
valid_names = re.compile(r"^[a-zA-Z0-9]+$")

class AWSObject(object):
    def __init__(
        self,
        name: str,
        type: Any = ...,
        dictname: str | None = ...,
        props: dict[str, Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def validate(self) -> None: ...
    def JSONrepr(self) -> dict[str, Any]: ...
    def to_json(self, indent: int | None = ..., sort_keys: bool = ...) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class AWSProperty(AWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    def __init__(self, **kwargs: Any) -> None: ...

class AWSHelperFn(object):
    def getdata(self, data: object) -> str | object: ...
    def to_json(self, indent: int | None = ..., sort_keys: bool = ...) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class awsencode(json.JSONEncoder):
    def default(self, obj: Any) -> Any: ...
