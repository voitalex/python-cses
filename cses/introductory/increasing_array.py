""" Increasing Array

Link: https://cses.fi/problemset/task/1094

You are given an array of n integers. You want to modify the array so that it is increasing,
i.e., every element is at least as large as the previous element.

On each turn, you may increase the value of any element by one. What is the minimum number of turns required?

Input :
  - The first input line contains an integer n: the size of the array.
  - Then, the second line contains n integers x1, x2, ..., xn: the contents of the array.

Output :
 - Print the minimum number of turns.

Constraints :
  - 1 <= n <= 2 * 10^5
  - 1 <= Xi <= 10^9

Example :

    Input:
    5
    3 2 5 1 7

    Output:
    5
"""

from typing import List


def increasing_array(numbers: List[int]) -> int:
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

    print(increasing_array(numbers))


if __name__ == '__main__':
    main()
