from generator import NumberGenerator
from settings import HELLO_RESPONSE


class API:
    """"
    Handlers for all commands.
    """
    def __init__(self, gen: NumberGenerator):
        self._gen = gen

    def hi(self):
        """
        Handles greetings command.
        """
        print(HELLO_RESPONSE)

    def get_random(self):
        """
        Handles generation command.
        """
        num = self._gen.generate()
        print(num)
