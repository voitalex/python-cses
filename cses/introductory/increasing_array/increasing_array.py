""" Increasing Array """

from typing import List


def solve(numbers: List[int]) -> int:
    """ Решение задачи """

    curr_max = numbers[0]
    result = 0

    for index in range(1, len(numbers)):
        if curr_max > numbers[index]:
            result += (curr_max - numbers[index])
        else:
            curr_max = numbers[index]

    return result


def main() -> None:
    """ Запуск решения """

    _ = int(input())
    numbers = [int(i) for i in input().split(' ')]

    print(solve(numbers))


if __name__ == '__main__':
    main()
