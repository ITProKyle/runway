"""This type stub file was generated by pyright."""

class RequestExceededException(Exception):
    def __init__(self, requested_amt, retry_time) -> None: ...

class RequestToken: ...

class TimeUtils:
    def time(self): ...
    def sleep(self, value): ...

class BandwidthLimiter:
    def __init__(self, leaky_bucket, time_utils=...) -> None: ...
    def get_bandwith_limited_stream(
        self, fileobj, transfer_coordinator, enabled=...
    ): ...

class BandwidthLimitedStream:
    def __init__(
        self,
        fileobj,
        leaky_bucket,
        transfer_coordinator,
        time_utils=...,
        bytes_threshold=...,
    ) -> None: ...
    def enable_bandwidth_limiting(self): ...
    def disable_bandwidth_limiting(self): ...
    def read(self, amount): ...
    def signal_transferring(self): ...
    def signal_not_transferring(self): ...
    def seek(self, where): ...
    def tell(self): ...
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs): ...

class LeakyBucket:
    def __init__(
        self, max_rate, time_utils=..., rate_tracker=..., consumption_scheduler=...
    ) -> None: ...
    def consume(self, amt, request_token): ...

class ConsumptionScheduler:
    def __init__(self) -> None: ...
    def is_scheduled(self, token): ...
    def schedule_consumption(self, amt, token, time_to_consume): ...
    def process_scheduled_consumption(self, token): ...

class BandwidthRateTracker:
    def __init__(self, alpha=...) -> None: ...
    @property
    def current_rate(self): ...
    def get_projected_rate(self, amt, time_at_consumption): ...
    def record_consumption_rate(self, amt, time_at_consumption): ...