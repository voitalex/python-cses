""" Tower of Hanoi

The Tower of Hanoi game consists of three stacks (left, middle and right) and n round disks of different sizes.
Initially, the left stack has all the disks, in increasing order of size from top to bottom.

The goal is to move all the disks to the right stack using the middle stack. On each move you can move
the uppermost disk from a stack to another stack. In addition, it is not allowed to place a larger disk
on a smaller disk.

Your task is to find a solution that minimizes the number of moves.

Input :
    The only input line has an integer n: the number of disks.

Output :
    First print an integer k: the minimum number of moves.

After this, print k lines that describe the moves.
Each line has two integers a and b: you move a disk from stack a to stack b.

Constraints :
    1 <= n <= 16

    Example :

    Input:
    2

    Output:
    3
    1 2
    1 3
    2 3
"""

from typing import Tuple, Generator


def tower_of_hanoi(
        disk: int,
        from_peg: int = 1,
        temp_peg: int = 2,
        to_peg: int = 3,
) -> Generator[Tuple[int, int], None, None]:
    """ Решение задачи """

    if disk <= 1:
        yield from_peg, to_peg
        return

    yield from tower_of_hanoi(disk - 1, from_peg=from_peg, temp_peg=to_peg, to_peg=temp_peg)
    yield from_peg, to_peg
    yield from tower_of_hanoi(disk - 1, from_peg=temp_peg, temp_peg=from_peg, to_peg=to_peg)


def main() -> None:
    """ Запуск решения """

    disks = int(input())
    moves = list(tower_of_hanoi(disks))

    print(len(moves))
    for (first, second) in moves:
        print(f'{first} {second}')


if __name__ == '__main__':
    main()
