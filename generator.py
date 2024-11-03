from random import randint


class NumberGenerator:
    def __init__(self, min_val, max_val):
        """
        :param min_val: minimum value in range (inclusive)
        :param max_val: maximum value in range (inclusive)
        """
        self._min_val = min_val
        self._max_val = max_val

    def generate(self):
        """"
        Generates random number in range [min_val, max_val]
        """
        pass


class IntGenerator(NumberGenerator):
    def generate(self) -> int:
        """"
        Generates random integer in range [min_val, max_val]
        """
        return randint(self._min_val, self._max_val)