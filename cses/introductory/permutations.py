""" Permutations

Link: https://cses.fi/problemset/task/1070

A permutation of integers 1, 2, ..., n is called beautiful if there are no adjacent elements
whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input :
 - The only input line contains an integer n.

Output :
  - Print a beautiful permutation of integers 1, 2, ..., n.
    If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints :
  - 1 <= n <= 1*10E6

Examples :

    Input: 5
    Output: 4 2 5 3 1

    Input:  3
    Output: NO SOLUTION
"""

from typing import Generator


def permutations(length: int) -> Generator[int, None, None]:
    """ Решение задачи """

    # Для последовательности из трех элементов или менее ответа не существует
    if length in (2, 3):
        return

    # Для реализации последовательности с указанными с условиями свойствами
    # достаточно возвращать сперва упорядоченные нечетные числа, а потом четные

    start_odds, start_evens = (length - 1, length) if length % 2 == 0 else (length, length - 1)

    yield from range(start_odds, 0, -2)
    yield from range(start_evens, 0, -2)


def main() -> None:
    """ Запуск решения """

    nums_count = int(input())
    print(' '.join(str(i) for i in permutations(nums_count)) or 'NO SOLUTION')


if __name__ == '__main__':
    main()
