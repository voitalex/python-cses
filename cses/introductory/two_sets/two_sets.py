""" Two Sets """

from typing import Tuple, Set


def solve(nums_count: int) -> Tuple[bool, Set[int], Set[int]]:
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
    possible, first_set, second_set = solve(n)

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
