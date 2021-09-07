""" Trailing Zeros

Link: https://cses.fi/problemset/task/1618

Your task is to calculate the number of trailing zeros in the factorial n!.

For example, 20!=2432902008176640000 and it has 4 trailing zeros.

Input :
    The only input line has an integer n.

Output :
    Print the number of trailing zeros in n!.

Constraints :
    1 <= n <= 10^9

Example :

    Input:
    20

    Output:
    4
"""


from itertools import starmap, repeat, count, takewhile
from math import floor


def trailing_zeros(factorial: int) -> int:
    """ Решение задачи """

    return sum(
        takewhile(
            lambda x: x > 0,
            map(
                lambda x: floor(factorial / x),
                starmap(pow, zip(repeat(5), count(1)))
            )
        )
    )


def main() -> None:
    """ Запуск решения """

    n = int(input())
    print(trailing_zeros(n))


if __name__ == '__main__':
    main()
