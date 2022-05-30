""" Two Sets """

import pytest
from two_sets import solve


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, (False, set(), set())),
        (2, (False, set(), set())),
        (3, (True, {3}, {1, 2})),
        (4, (True, {4, 1}, {2, 3})),
        (5, (False, set(), set())),
        (6, (False, set(), set())),
        (155974, (False, set(), set())),
    ]
)
def test_two_sets(value, expected):

    result_possible, result_first, result_second = solve(value)
    expected_possible, expected_first, expected__second = expected

    assert result_possible == expected_possible and \
           (result_first in [expected_first, result_first]) and \
           (result_second in [expected_first, expected__second])
