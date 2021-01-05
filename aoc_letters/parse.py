"""
Parsing functions to identify characters from visual outputs.

"""
from typing import List, Generator, Iterable

from aoc_letters.mappings import mappings


def _chunks(lst, n) -> Generator[int]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def _format_row(row: Iterable[int]) -> str:
    row = ''.join('#' if char == 1 else ' ' for char in row)
    return row


def letter(text: Iterable[Iterable[int]]) -> str:
    """
    Parse a visual letter into a character. 6 Rows should be given as
    a 5 item list with a 1 to indicate a filled cell.

    Parameters
    ----------
    text: List of rows.

    Returns
    -------
    solution: str

    """
    rows = [_format_row(row) for row in text]
    text = '\n'.join(rows)
    solution = mappings[text]
    return solution


def word(rows: List[List[int]]) -> str:
    """
    Parse a visual word into a character. 6 Rows should be given as
    a list with a 1 to indicate a filled cell.

    Parameters
    ----------
    rows: List of rows.

    Returns
    -------
    solution: str

    """
    chars = (_chunks(row, 5) for row in rows)
    letters = zip(*chars)
    answer = (letter(char) for char in letters)
    return ''.join(answer)
