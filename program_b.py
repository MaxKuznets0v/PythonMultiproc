import subprocess
import sys
from settings import HELLO_CMD, HELLO_RESPONSE, NUM_SAMPLES, GET_RANDOM_CMD, TERMINATE_CMD


def send_message(process: subprocess.Popen, message: str) -> None:
    """
    Writes given message into the process' stdin.
    :param process: current opened process.
    :param message: message as a string.
    """
    process.stdin.write(f"{message}\n".encode())
    process.stdin.flush()


def receive_message(process: subprocess.Popen) -> str:
    """
    Reads next line from the process' stdout.
    :param process: current opened process.
    :return: read message.
    """
    return process.stdout.readline().decode().strip()


def calc_median(sorted_nums: list) -> float:
    """
    Calculates median of a sorted list.
    :param sorted_nums: sorted list of numbers.
    :return: median value. 0 if list is empty, takes 2 middle elements if length is even.
    """
    size = len(sorted_nums)
    if size == 0:
        return 0

    if size % 2 == 0:
        median = (sorted_nums[size // 2] + sorted_nums[size // 2 - 1]) / 2
    else:
        median = sorted_nums[size // 2]

    return median


def calc_average(nums: list) -> float:
    """
    Calculates average value from a given list.
    :param nums: list of numbers.
    :return: mean value.
    """
    size = len(nums)
    if size == 0:
        return 0

    return sum(nums) / size


if __name__ == "__main__":
    process_a = subprocess.Popen([sys.executable, "program_a.py"], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)

    # Testing Hi command.
    send_message(process_a, HELLO_CMD)
    answer = receive_message(process_a)
    assert answer == HELLO_RESPONSE

    # Generating random integers.
    random_nums = list()
    for i in range(NUM_SAMPLES):
        send_message(process_a, GET_RANDOM_CMD)
        num = int(receive_message(process_a))
        random_nums.append(num)

    send_message(process_a, TERMINATE_CMD)
    process_a.wait()

    # Sorting and printing generated numbers.
    random_nums.sort()
    print("Generated list: ", *random_nums)

    # Calculating statistics.
    median = calc_median(random_nums)
    average = calc_average(random_nums)
    print(f"Median: {median}")
    print(f"Average: {average}")
