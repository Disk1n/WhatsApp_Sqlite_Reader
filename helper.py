from datetime import datetime

def timestamp_to_apple(ts: float) -> datetime:
    """Convert a Unix timestamp to Apple's NSDate (offset from 2001-01-01)."""
    return datetime.fromtimestamp(ts) + (datetime(2001, 1, 1) - datetime.fromtimestamp(0))
