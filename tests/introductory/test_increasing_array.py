""" Increasing Array """

import pytest
from cses.introductory.increasing_array import increasing_array


@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0),
        ([1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1], 8999999991),
        ([6, 10, 4, 10, 2, 8, 9, 2, 7, 7], 31),
        ([329873232], 0),
    ]
)
def test_increasing_array(value, expected):
    assert increasing_array(value) == expected
