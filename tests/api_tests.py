import pytest
from api import API
from generator import IntGenerator
from settings import MIN_GEN_VAL, MAX_GEN_VAL

@pytest.fixture()
def api():
    gen = IntGenerator(MIN_GEN_VAL, MAX_GEN_VAL)
    return API(gen)


def test_hello_output(api, capsys):
    api.hi()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hi"

    api.hi()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hi"


def test_get_random(api, capsys):
    api.get_random()
    captured = capsys.readouterr()
    assert MIN_GEN_VAL <= int(captured.out.strip()) <= MAX_GEN_VAL
