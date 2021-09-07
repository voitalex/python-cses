""" Missing Number

Link: https://cses.fi/problemset/task/1083

You are given all numbers between 1, 2, ... ,n except one. Your task is to find the missing number.

Input :
  - The first input line contains an integer n.
  - The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output :
- Print the missing number.

Constraints :
  - 2 <= n <= 2*10^5

Example :

    Input:
    5
    2 3 1 5

    Output:
    4
"""

from typing import List


def missing_number(count: int, numbers: List[int]) -> int:
    """ Решение задачи """

    sum_of_numbers = count * (count + 1) // 2
    for number in numbers:
        sum_of_numbers -= number

    return sum_of_numbers


def main():
    """ Запуск решения """

    numbers_count = int(input())
    numbers: List[int] = [int(s) for s in input().split(' ')]
    print(missing_number(numbers_count, numbers))


if __name__ == '__main__':
    main()
