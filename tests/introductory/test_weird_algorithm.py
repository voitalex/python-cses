""" Weird Algorithm """

import pytest
from cses.introductory.weird_algorithm import weird_algorithm


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, [1]),
        (5, [5, 16, 8, 4, 2, 1]),
        (7, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        (15, [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
    ]
)
def test_weird_algorithm(value, expected):
    assert list(weird_algorithm(value)) == expected
