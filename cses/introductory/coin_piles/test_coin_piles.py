""" Coin Piles """

import pytest
from coin_piles import solve


@pytest.mark.parametrize(
    'first, second, expected',
    [
        (0, 0, True),
        (0, 1, False),
        (0, 2, False),
        (842572599, 577431753, True),
        (733431661, 716735123, True),
        (409325692, 74067624, False),
        (753728522, 940667932, True),
        (11, 4, False),
    ]
)
def test_coin_piles(first, second, expected):
    assert solve(first, second) == expected
