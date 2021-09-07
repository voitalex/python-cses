""" Bit Strings

Link: https://cses.fi/problemset/task/1617

Your task is to calculate the number of bit strings of length n.

For example, if n=3, the correct answer is 8, because the possible bit strings are :
    000, 001, 010, 011, 100, 101, 110, and 111.

Input :
    The only input line has an integer n.

Output :
    Print the result modulo 10^9+7.

Constraints :
    1 <= n <= 10^6

Example :

    Input:
    3

    Output:
    8
"""


def bit_strings(length: int) -> int:
    """ Решение задачи """
    return (2 ** length) % (10 ** 9 + 7)


def main() -> None:
    """ Запуск решения """

    length = int(input())
    print(bit_strings(length))


if __name__ == '__main__':
    main()
