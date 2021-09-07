""" Two Knights """

import pytest
from cses.introductory.two_knights import two_knights


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, 0),
        (2, 6),
        (3, 28),
        (4, 96),
        (5, 252),
        (6, 550),
        (7, 1056),
    ]
)
def test_two_knights(value, expected):
    assert two_knights(value) == expected
