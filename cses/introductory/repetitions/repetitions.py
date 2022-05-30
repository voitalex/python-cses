""" Repetitions """

import functools


def _longest_string(curr, next_char):
    curr_char, curr_count, max_count = curr
    if curr_char != next_char:
        return next_char, 1, max(curr_count, max_count)

    return curr_char, curr_count + 1, max(curr_count + 1, max_count)


def solve(chars: str) -> int:
    """ Решение задачи """

    _, _, res = functools.reduce(_longest_string, chars, ('', 1, 0))

    return res


def main():
    """ Запуск решения """

    string = input()
    print(solve(string))


if __name__ == '__main__':
    main()
