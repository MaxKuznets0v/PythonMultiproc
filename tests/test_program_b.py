import pytest
import subprocess
import sys
import os
from statistics import median, mean
from program_b import calc_median, calc_average, send_message, receive_message


@pytest.fixture()
def dummy_read_print() -> subprocess.Popen:
    return subprocess.Popen(
        [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "dummy_read_print.py")],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def test_send_receive_message(dummy_read_print):
    send_message(dummy_read_print, "TEST message")
    assert receive_message(dummy_read_print) == "TEST message"

    send_message(dummy_read_print, "second message")
    assert receive_message(dummy_read_print) == "second message"

    send_message(dummy_read_print, "STOP")
    assert receive_message(dummy_read_print) == ""
    assert receive_message(dummy_read_print) == ""
    with pytest.raises(OSError):
        send_message(dummy_read_print, "this cannot be delivered")

    assert receive_message(dummy_read_print) == ""


def test_stats():
    nums = [10, -1, 5, 6, 11, 6]
    assert calc_median(sorted(nums)) == median(nums)
    assert calc_average(nums) == mean(nums)
