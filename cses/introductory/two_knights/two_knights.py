""" Two Knights """

from functools import lru_cache


@lru_cache()
def _calculate_attack_positions(size: int) -> int:
    """ Вычисляет количество позиций, на которых два коня атакуют друг друга """

    if size <= 2:
        return 0

    return _calculate_attack_positions(size - 1) + 8 * (size - 2)


def solve(size: int) -> int:
    """ Решение задачи """

    all_positions = (size * size) * (size * size - 1) // 2
    attacked_positions = _calculate_attack_positions(size)

    return all_positions - attacked_positions


def main() -> None:
    """ Запуск решения """

    max_chessboard_size = int(input())
    for chessboard_size in range(1, max_chessboard_size+1):
        print(solve(chessboard_size))


if __name__ == '__main__':
    main()
