""" Missing Number """

import pytest
from missing_number import solve


@pytest.mark.parametrize(
    'count, numbers, expected',
    [
        (2, [1], 2),
        (5, [5, 2, 1, 3], 4),
        (10, [2, 8, 10, 6, 5, 1, 3, 7, 4], 9),
    ]
)
def test_missing_number(count, numbers, expected):
    assert solve(count, numbers) == expected
