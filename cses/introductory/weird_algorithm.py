""" Weird Algorithm

Link: https://cses.fi/problemset/task/1068

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two,
and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one.

For example, the sequence for n=3 is as follows: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Your task is to simulate the execution of the algorithm for a given value of n.

Input :
  - The only input line contains an integer n.

Output :
  - Print a line that contains all values of n during the algorithm.

Constraints :
  - 1 <= n <= 10E6

Example :
  Input: 3
  Output: 3 10 5 16 8 4 2 1
"""

from typing import Iterator


def weird_algorithm(start: int) -> Iterator[int]:
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
    print(' '.join(map(str, weird_algorithm(start))))


if __name__ == '__main__':
    main()
