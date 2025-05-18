from datetime import datetime
from helper import timestamp_to_apple

def test_unix_epoch_converts_to_apple_epoch():
    assert timestamp_to_apple(0) == datetime(2001, 1, 1)
