import pytest
import subprocess
import sys
from statistics import median, mean
from program_b import calc_median, calc_average, send_message, receive_message
from settings import TERMINATE_CMD


@pytest.fixture()
def dummy_read_print() -> subprocess.Popen:
    return subprocess.Popen([sys.executable, "dummy_read_print.py"], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)


def test_send_receive_message(dummy_read_print):
    send_message(dummy_read_print, "TEST message")
    assert receive_message(dummy_read_print) == "TEST message"

    send_message(dummy_read_print, "second message")
    assert receive_message(dummy_read_print) == "second message"

    send_message(dummy_read_print, TERMINATE_CMD)
    assert receive_message(dummy_read_print) == ""
    assert receive_message(dummy_read_print) == ""
    with pytest.raises(OSError):
        send_message(dummy_read_print, "this cannot be delivered")

    assert receive_message(dummy_read_print) == ""


def test_stats():
    nums = [10, -1, 5, 6, 11, 6]
    assert calc_median(sorted(nums)) == median(nums)
    assert calc_average(nums) == mean(nums)
