"""Tests for runway.cfngin.hooks.base."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, call, patch

import pytest

from runway.cfngin.exceptions import StackFailed
from runway.cfngin.hooks.base import Hook, HookDeployAction, HookDestroyAction
from runway.cfngin.status import (
    COMPLETE,
    FAILED,
    SKIPPED,
    SUBMITTED,
    CompleteStatus,
    SubmittedStatus,
)

if TYPE_CHECKING:
    from ...factories import MockCfnginContext

COMPLETE_W_REASON = CompleteStatus("test successful")


class TestHook:
    """Tests for runway.cfngin.hooks.base.Hook."""

    def test_attributes(self, cfngin_context: MockCfnginContext) -> None:
        """Test attributes set during __init__."""
        provider = MagicMock()
        args = {"tags": {"key": "val"}}
        result = Hook(cfngin_context, provider, **args)

        assert result.args.tags["key"] == "val"  # type: ignore
        assert result.args.tags == {"cfngin_namespace": "example", "key": "val"}
        assert not result.blueprint
        assert result.context == cfngin_context
        assert result.provider == provider
        assert not result.stack
        assert result.stack_name == "stack"

    def test_tags(self, cfngin_context: MockCfnginContext) -> None:
        """Test tags property."""
        cfngin_context.config.tags = {"context_tag": "val"}

        hook = Hook(cfngin_context, MagicMock(), tags={"arg_tag": "val"})

        assert hook.tags.to_dict() == [
            {"Key": "arg_tag", "Value": "val"},
            {"Key": "context_tag", "Value": "val"},
        ]

    def test_get_template_description(self, cfngin_context: MockCfnginContext) -> None:
        """Test for get_template_description."""
        hook = Hook(cfngin_context, MagicMock())

        result = hook.get_template_description()

        assert result == f"Automatically generated by {hook.__class__.__module__}"
        assert hook.get_template_description("suffix").endswith(" - suffix")

    @patch(
        "runway.cfngin.hooks.base.HookDeployAction.run",
        MagicMock(return_value=COMPLETE),
    )
    def test_deploy_stack(
        self, cfngin_context: MockCfnginContext, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test for deploy_stack."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock()
        stack.name = "test-stack"

        with caplog.at_level(logging.INFO, logger="runway.cfngin.hooks.base"):
            assert hook.deploy_stack(stack=stack, wait=False) == COMPLETE

        assert caplog.records[0].message == f"{stack.name}:{COMPLETE.name}"

    @patch(
        "runway.cfngin.hooks.base.HookDeployAction.run",
        MagicMock(side_effect=[SUBMITTED, COMPLETE]),
    )
    def test_deploy_stack_wait(
        self, cfngin_context: MockCfnginContext, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test for deploy_stack with wait."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock()
        stack.name = "test-stack"

        with caplog.at_level(logging.DEBUG, logger="runway.cfngin.hooks.base"):
            assert hook.deploy_stack(stack=stack, wait=True) == COMPLETE

        assert caplog.records[0].message == f"{stack.name}:{SUBMITTED.name}"
        assert caplog.records[1].message == "waiting for stack to complete..."
        assert caplog.records[2].message == f"{stack.name}:{COMPLETE.name}"

    @patch(
        "runway.cfngin.hooks.base.HookDeployAction.run",
        MagicMock(side_effect=[SKIPPED]),
    )
    def test_deploy_stack_wait_skipped(
        self, cfngin_context: MockCfnginContext, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test for deploy_stack with wait and skip."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock()
        stack.name = "test-stack"

        with caplog.at_level(logging.INFO, logger="runway.cfngin.hooks.base"):
            assert hook.deploy_stack(stack=stack, wait=True) == SKIPPED

        assert caplog.records[0].message == f"{stack.name}:{SKIPPED.name}"

    @patch("runway.cfngin.hooks.base.HookDeployAction.run", MagicMock(side_effect=[FAILED]))
    def test_deploy_stack_wait_failed(self, cfngin_context: MockCfnginContext) -> None:
        """Test for deploy_stack with wait and skip."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock()
        stack.name = "test-stack"

        with pytest.raises(StackFailed):
            assert hook.deploy_stack(stack=stack, wait=True) == FAILED

    @patch(
        "runway.cfngin.hooks.base.HookDestroyAction.run",
        MagicMock(side_effect=[SUBMITTED, COMPLETE_W_REASON]),
    )
    def test_destroy_stack(
        self, cfngin_context: MockCfnginContext, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test for destroy_stack with wait."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock()
        stack.name = "test-stack"

        with caplog.at_level(logging.DEBUG, logger="runway.cfngin.hooks.base"):
            assert hook.destroy_stack(stack=stack, wait=True) == COMPLETE

        assert caplog.records[0].message == f"{stack.name}:{SUBMITTED.name}"
        assert caplog.records[1].message == "waiting for stack to complete..."
        assert (
            caplog.records[2].message
            == f"{stack.name}:{COMPLETE_W_REASON.name} ({COMPLETE_W_REASON.reason})"
        )

    def test_wait_for_stack_till_reason(self, cfngin_context: MockCfnginContext) -> None:
        """Test _wait_for_stack till_reason option."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock(fqn="test-stack", name="stack")
        action = MagicMock()
        action.run.side_effect = [
            SUBMITTED,
            SubmittedStatus("not yet"),
            SubmittedStatus("catch"),
            COMPLETE,
        ]

        result = hook._wait_for_stack(action, stack=stack, till_reason="catch")
        assert result == SUBMITTED
        assert result.reason == "catch"

    def test_wait_for_stack_log_change(
        self, cfngin_context: MockCfnginContext, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test _wait_for_stack log status change."""
        hook = Hook(cfngin_context, MagicMock())
        stack = MagicMock(fqn="test-stack", name="stack")
        new_status = SubmittedStatus("new")
        action = MagicMock()
        action.run.side_effect = [new_status, COMPLETE]
        mock_log = MagicMock()

        monkeypatch.setattr(hook, "_log_stack", mock_log)

        hook._wait_for_stack(
            action,
            last_status=SubmittedStatus("original"),
            stack=stack,
            till_reason="catch",
        )

        mock_log.assert_has_calls([call(stack, new_status), call(stack, COMPLETE)])
        assert mock_log.call_count == 2

    def test_post_deploy(self, cfngin_context: MockCfnginContext) -> None:
        """Test post_deploy."""
        hook = Hook(cfngin_context, MagicMock())

        with pytest.raises(NotImplementedError):
            hook.post_deploy()

    def test_post_destroy(self, cfngin_context: MockCfnginContext) -> None:
        """Test post_destroy."""
        hook = Hook(cfngin_context, MagicMock())

        with pytest.raises(NotImplementedError):
            hook.post_destroy()

    def test_pre_deploy(self, cfngin_context: MockCfnginContext) -> None:
        """Test pre_deploy."""
        hook = Hook(cfngin_context, MagicMock())

        with pytest.raises(NotImplementedError):
            hook.pre_deploy()

    def test_pre_destroy(self, cfngin_context: MockCfnginContext) -> None:
        """Test pre_destroy."""
        hook = Hook(cfngin_context, MagicMock())

        with pytest.raises(NotImplementedError):
            hook.pre_destroy()


class TestHookDeployAction:
    """Tests for runway.cfngin.hooks.base.HookDeployAction."""

    def test_provider(self, cfngin_context: MockCfnginContext) -> None:
        """Test provider property."""
        provider = MagicMock()
        obj = HookDeployAction(cfngin_context, provider)

        assert obj.provider == provider

    def test_build_provider(self, cfngin_context: MockCfnginContext) -> None:
        """Test build_provider."""
        provider = MagicMock()
        obj = HookDeployAction(cfngin_context, provider)

        assert obj.build_provider() == provider

    def test_run(self, cfngin_context: MockCfnginContext, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test run."""
        obj = HookDeployAction(cfngin_context, MagicMock())
        monkeypatch.setattr(obj, "_launch_stack", lambda: "success")

        assert obj.run() == "success"


class TestHookDestroyAction:
    """Tests for runway.cfngin.hooks.base.HookDestroyAction."""

    def test_run(self, cfngin_context: MockCfnginContext, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test run."""
        obj = HookDestroyAction(cfngin_context, MagicMock())
        monkeypatch.setattr(obj, "_destroy_stack", lambda: "success")

        assert obj.run() == "success"
