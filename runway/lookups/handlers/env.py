"""Retrieve a value from an environment variable."""

# pyright: reportIncompatibleMethodOverride=none
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from .base import LookupHandler

if TYPE_CHECKING:
    from typing_extensions import Literal

    from ...context import CfnginContext, RunwayContext


class EnvLookup(LookupHandler):
    """Environment variable Lookup."""

    TYPE_NAME: Final[Literal["env"]] = "env"
    """Name that the Lookup is registered as."""

    @classmethod
    def handle(
        cls,
        value: str,
        context: CfnginContext | RunwayContext,
        *__args: Any,
        **__kwargs: Any,
    ) -> Any:
        """Retrieve an environment variable.

        The value is retrieved from a copy of the current environment variables
        that is saved to the context object. These environment variables
        are manipulated at runtime by Runway to fill in additional values
        such as ``DEPLOY_ENVIRONMENT`` and ``AWS_REGION`` to match the
        current execution.

        Args:
            value: The value passed to the Lookup.
            context: The current context object.

        Raises:
            ValueError: Unable to find a value for the provided query and
                a default value was not provided.

        """
        query, args = cls.parse(value)

        result = context.env.vars.get(query, args.pop("default", ""))

        if result != "":  # allows for False bool and NoneType results
            return cls.format_results(result, **args)

        raise ValueError(f'"{value}" does not exist in the environment')
