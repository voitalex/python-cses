""" Bit Strings """

import pytest
from bit_strings import solve


@pytest.mark.parametrize(
    'value, expected',
    [
        (7, 128),
        (15, 32768),
        (255, 396422633),
        (270271, 26708571),
        (704511, 852098711),
    ]
)
def test_bit_strings(value, expected):
    assert solve(value) == expected
