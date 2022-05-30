""" Tower of Hanoi """

import pytest
from tower_of_hanoi import solve


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, [(1, 3)]),
        (2, [(1, 2), (1, 3), (2, 3)]),
        (3, [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)])

    ]
)
def test_tower_of_hanoi(value, expected):
    assert list(solve(value)) == expected
