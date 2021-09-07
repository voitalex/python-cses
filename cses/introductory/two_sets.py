""" Two Sets

Link: https://cses.fi/problemset/task/1092

Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input :
    The only input line contains an integer n.

Output :
    Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets.
First, print the number of elements in the first set followed by the elements themselves
in a separate line, and then, print the second set in a similar way.

Constraints
    1 <= n <= 10^6

Example 1 :

    Input:
    7

    Output:
    YES
    4
    1 2 4 7
    3
    3 5 6

Example 2 :

    Input:
    6

    Output:
    NO
"""

from typing import Tuple, Set


def two_sets(nums_count: int) -> Tuple[bool, Set[int], Set[int]]:
    """ Решение задачи """

    nums_sum = (nums_count + 1) * nums_count // 2
    if nums_sum % 2 > 0:
        return False, set(), set()

    half_sum = nums_sum // 2
    all_nums = set(range(1, nums_count + 1))
    taken_nums = set()

    x = nums_count
    while half_sum > 0:
        if half_sum - x >= 0:
            half_sum -= x
            all_nums.discard(x)
            taken_nums.add(x)
        x -= 1

    return True, all_nums, taken_nums


def main() -> None:
    """ Запуск решения """

    n = int(input())
    possible, first_set, second_set = two_sets(n)

    if not possible:
        print('NO')
    else:
        print('YES')
        print(len(first_set))
        print(' '.join(str(i) for i in first_set))
        print(len(second_set))
        print(' '.join(str(i) for i in second_set))


if __name__ == '__main__':
    main()
