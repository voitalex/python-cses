""" Permutations """

import pytest
from permutations import solve


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, [1]),
        (2, []),
        (3, []),
        (6, [5, 3, 1, 6, 4, 2]),
        (8, [7, 5, 3, 1, 8, 6, 4, 2]),
        (9, [9, 7, 5, 3, 1, 8, 6, 4, 2]),
    ]
)
def test_permutations(value, expected):
    assert list(solve(value)) == expected
