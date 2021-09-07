""" Number Spiral """

import pytest
from cses.introductory.number_spiral import number_spiral


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (170550340, 943050741, 889344699930098742),
        (121998376, 943430501, 890061110095112626),
        (689913499, 770079066, 593021767041187724),
        (586095107, 933655238, 871712102163621276),

    ]
)
def test_number_spiral(x, y, expected):
    assert number_spiral(y, x) == expected
