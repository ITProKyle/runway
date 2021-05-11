"""This type stub file was generated by pyright."""
from __future__ import annotations

import collections
import contextlib
import multiprocessing
from multiprocessing.managers import BaseManager
from typing import TYPE_CHECKING

from .futures import BaseTransferFuture, BaseTransferMeta

if TYPE_CHECKING:
    from logging import Logger

logger: Logger = ...
SHUTDOWN_SIGNAL = ...
DownloadFileRequest = collections.namedtuple(
    "DownloadFileRequest",
    ["transfer_id", "bucket", "key", "filename", "extra_args", "expected_size"],
)
GetObjectJob = collections.namedtuple(
    "GetObjectJob",
    [
        "transfer_id",
        "bucket",
        "key",
        "temp_filename",
        "extra_args",
        "offset",
        "filename",
    ],
)

@contextlib.contextmanager
def ignore_ctrl_c(): ...

class ProcessTransferConfig:
    def __init__(
        self,
        multipart_threshold=...,
        multipart_chunksize=...,
        max_request_processes=...,
    ) -> None: ...

class ProcessPoolDownloader:
    def __init__(self, client_kwargs=..., config=...) -> None: ...
    def download_file(
        self, bucket, key, filename, extra_args=..., expected_size=...
    ): ...
    def shutdown(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, *args): ...

class ProcessPoolTransferFuture(BaseTransferFuture):
    def __init__(self, monitor, meta) -> None: ...
    @property
    def meta(self): ...
    def done(self): ...
    def result(self): ...
    def cancel(self): ...

class ProcessPoolTransferMeta(BaseTransferMeta):
    def __init__(self, transfer_id, call_args) -> None: ...
    @property
    def call_args(self): ...
    @property
    def transfer_id(self): ...
    @property
    def user_context(self): ...

class ClientFactory:
    def __init__(self, client_kwargs=...) -> None: ...
    def create_client(self): ...

class TransferMonitor:
    def __init__(self) -> None: ...
    def notify_new_transfer(self): ...
    def is_done(self, transfer_id): ...
    def notify_done(self, transfer_id): ...
    def poll_for_result(self, transfer_id): ...
    def notify_exception(self, transfer_id, exception): ...
    def notify_cancel_all_in_progress(self): ...
    def get_exception(self, transfer_id): ...
    def notify_expected_jobs_to_complete(self, transfer_id, num_jobs): ...
    def notify_job_complete(self, transfer_id): ...

class TransferState:
    def __init__(self) -> None: ...
    @property
    def done(self): ...
    def set_done(self): ...
    def wait_till_done(self): ...
    @property
    def exception(self): ...
    @exception.setter
    def exception(self, val): ...
    @property
    def jobs_to_complete(self): ...
    @jobs_to_complete.setter
    def jobs_to_complete(self, val): ...
    def decrement_jobs_to_complete(self): ...

class TransferMonitorManager(BaseManager): ...

class BaseS3TransferProcess(multiprocessing.Process):
    def __init__(self, client_factory) -> None: ...
    def run(self): ...

class GetObjectSubmitter(BaseS3TransferProcess):
    def __init__(
        self,
        transfer_config,
        client_factory,
        transfer_monitor,
        osutil,
        download_request_queue,
        worker_queue,
    ) -> None: ...

class GetObjectWorker(BaseS3TransferProcess):
    _MAX_ATTEMPTS = ...
    _IO_CHUNKSIZE = ...
    def __init__(self, queue, client_factory, transfer_monitor, osutil) -> None: ...
