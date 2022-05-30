""" Missing Number """

from typing import List


def solve(count: int, numbers: List[int]) -> int:
    """ Решение задачи """

    sum_of_numbers = count * (count + 1) // 2
    for number in numbers:
        sum_of_numbers -= number

    return sum_of_numbers


def main():
    """ Запуск решения """

    numbers_count = int(input())
    numbers = [int(s) for s in input().split(' ')]
    print(solve(numbers_count, numbers))


if __name__ == '__main__':
    main()
