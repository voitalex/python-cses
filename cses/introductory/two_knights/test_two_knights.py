""" Two Knights """

import pytest
from two_knights import solve


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
    assert solve(value) == expected
