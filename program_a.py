from api import API
from generator import IntGenerator
from settings import HELLO_CMD, GET_RANDOM_CMD, TERMINATE_CMD, MIN_GEN_VAL, MAX_GEN_VAL


def run(api: API) -> None:
    """"
    Maps each command to corresponding API method.
    """
    while True:
        command = input().strip()
        if command == HELLO_CMD:
            api.hi()
        elif command == GET_RANDOM_CMD:
            api.get_random()
        elif command == TERMINATE_CMD:
            break


if __name__ == "__main__":
    int_gen = IntGenerator(MIN_GEN_VAL, MAX_GEN_VAL)
    api = API(int_gen)
    run(api)
