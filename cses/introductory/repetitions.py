""" Repetitions

Link: https://cses.fi/problemset/task/1069

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find
the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input :
- The only input line contains a string of n characters.

Output :
- Print one integer: the length of the longest repetition.

Constraints :
  - 1 = <= n < 10E6

Example :
  Input: ATTCGGGA
  Output: 3
"""

import functools


def _longest_string(curr, next_char):
    curr_char, curr_count, max_count = curr
    if curr_char != next_char:
        return next_char, 1, max(curr_count, max_count)

    return curr_char, curr_count + 1, max(curr_count + 1, max_count)


def repetitions(chars: str) -> int:
    """ Решение задачи """

    _, _, res = functools.reduce(_longest_string, chars, ('', 1, 0))

    return res


def main():
    """ Запуск решения """

    string = input()
    print(repetitions(string))


if __name__ == '__main__':
    main()
