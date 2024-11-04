import pytest
from generator import IntGenerator
from settings import MIN_GEN_VAL, MAX_GEN_VAL


num_generations = 10000


@pytest.fixture()
def generator() -> IntGenerator:
    return IntGenerator(MIN_GEN_VAL, MAX_GEN_VAL)


def test_generate_inside_range(generator):
    for i in range(num_generations):
        assert MIN_GEN_VAL <= generator.generate() <= MAX_GEN_VAL


def test_generate_small_range(generator):
    generator.set_range(0, 0)
    for i in range(num_generations):
        assert generator.generate() == 0

    generator.set_range(0, 1)
    for i in range(num_generations):
        num = generator.generate()
        assert num == 0 or num == 1


def test_generate_negative(generator):
    generator.set_range(-100, -10)
    for i in range(num_generations):
        assert generator.generate() < 0

    generator.set_range(-100, -50)
    for i in range(num_generations):
        assert -100 <= generator.generate() <= -50


def test_generate_ints(generator):
    for i in range(num_generations):
        assert generator.generate().__class__ is int


def test_set_range(generator):
    assert generator._min_val == MIN_GEN_VAL
    assert generator._max_val == MAX_GEN_VAL

    generator.set_range(1, 10)
    assert generator._min_val == 1
    assert generator._max_val == 10

    generator.set_range(-10, 10)
    assert generator._min_val == -10
    assert generator._max_val == 10

    with pytest.raises(ValueError):
        generator.set_range(10, 1)

    assert generator._min_val == -10
    assert generator._max_val == 10

    generator.set_range(5, 5)
    assert generator._min_val == 5
    assert generator._max_val == 5

def test_invalid_range_creation():
    with pytest.raises(ValueError):
        IntGenerator(-1, -10)

    IntGenerator(-5, -5)
