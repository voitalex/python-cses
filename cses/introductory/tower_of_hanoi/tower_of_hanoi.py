""" Tower of Hanoi """

from typing import Tuple, Generator


def solve(
        disk: int,
        from_peg: int = 1,
        temp_peg: int = 2,
        to_peg: int = 3,
) -> Generator[Tuple[int, int], None, None]:
    """ Решение задачи """

    if disk <= 1:
        yield from_peg, to_peg
        return

    yield from solve(disk - 1, from_peg=from_peg, temp_peg=to_peg, to_peg=temp_peg)
    yield from_peg, to_peg
    yield from solve(disk - 1, from_peg=temp_peg, temp_peg=from_peg, to_peg=to_peg)


def main() -> None:
    """ Запуск решения """

    disks = int(input())
    moves = list(solve(disks))

    print(len(moves))
    for (first, second) in moves:
        print(f'{first} {second}')


if __name__ == '__main__':
    main()
