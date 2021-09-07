""" Repetitions """

import pytest
from cses.introductory.repetitions import repetitions


@pytest.mark.parametrize(
    'value, expected',
    [
        ('AAAAAAAAAA', 10),
        ('ACACACACAC', 1),
        ('ACCGGGTTTT', 4),
        ('CTCAGGTCCG', 2),
        ('A', 1),
    ]
)
def test_repetitions(value, expected):
    assert repetitions(value) == expected
