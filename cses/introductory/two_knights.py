""" Two Knights

Link: https://cses.fi/problemset/task/1072

Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard
so that they do not attack each other.

Input :
    The only input line contains an integer n.

Output :
    Print n integers: the results.

Constraints :
    1 <= n <= 10000

Example :

    Input:
    8

    Output:
    0
    6
    28
    96
    252
    550
    1056
    1848
"""

from functools import lru_cache


@lru_cache()
def _calculate_attack_positions(size: int) -> int:
    """ Вычисляет количество позиций, на которых два коня атакуют друг друга """

    if size <= 2:
        return 0

    return _calculate_attack_positions(size - 1) + 8 * (size - 2)


def two_knights(size: int) -> int:
    """ Решение задачи """

    all_positions = (size * size) * (size * size - 1) // 2
    attacked_positions = _calculate_attack_positions(size)

    return all_positions - attacked_positions


def main() -> None:
    """ Запуск решения """

    max_chessboard_size = int(input())
    for chessboard_size in range(1, max_chessboard_size+1):
        print(two_knights(chessboard_size))


if __name__ == '__main__':
    main()
