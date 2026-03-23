from datetime import datetime, timezone

DEFAULT_TIMESTAMP_FMT = "%Y-%m-%dT%H:%M:%S"


def now() -> datetime:
    return datetime.now(timezone.utc)


def format_timestamp(timestamp, fmt: str = DEFAULT_TIMESTAMP_FMT) -> str:
    return timestamp.strftime(fmt)


def get_now_formatted(fmt: str = DEFAULT_TIMESTAMP_FMT) -> str:
    return format_timestamp(now(), fmt)
