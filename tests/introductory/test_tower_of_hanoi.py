""" Tower of Hanoi """

import pytest
from cses.introductory.tower_of_hanoi import tower_of_hanoi


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, [(1, 3)]),
        (2, [(1, 2), (1, 3), (2, 3)]),
        (3, [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)])

    ]
)
def test_tower_of_hanoi(value, expected):
    assert list(tower_of_hanoi(value)) == expected
