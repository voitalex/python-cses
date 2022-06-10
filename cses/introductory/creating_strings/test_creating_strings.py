""" Creating Strings """

import pytest
from creating_strings import solve


@pytest.mark.parametrize(
    'value, expected',
    [
        ('a', ['a']),
        ('ab', ['ab', 'ba']),
        ('abb', ['abb', 'bab', 'bba']),
        ('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
        (
            'aabac',
            [
                'aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba',
                'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa'
            ],
        ),
    ]
)
def test_creating_strings(value, expected):
    assert list(solve(value)) == expected
