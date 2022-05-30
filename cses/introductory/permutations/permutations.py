""" Permutations """

from typing import Generator


def solve(length: int) -> Generator[int, None, None]:
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
    print(' '.join(str(i) for i in solve(nums_count)) or 'NO SOLUTION')


if __name__ == '__main__':
    main()
