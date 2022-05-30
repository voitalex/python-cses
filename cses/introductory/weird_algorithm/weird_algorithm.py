""" Weird Algorithm """

from typing import Iterator


def solve(start: int) -> Iterator[int]:
    """ Решение задачи """
    element = start
    while True:
        yield element
        if element == 1:
            break
        element = element // 2 if element % 2 == 0 else 3 * element + 1


def main() -> None:
    """ Запуск решения """

    start = int(input())
    print(' '.join(map(str, solve(start))))


if __name__ == '__main__':
    main()
