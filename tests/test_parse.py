import pytest

from aoc_letters import parse


@pytest.mark.parametrize('text', [
    [[1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0]]
])
def test_letter(text):
    assert parse.letter(text) == 'E'


def test_word():
    rows = [
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]]
    assert parse.word(rows) == 'EF'
