""" Number Spiral

Link: https://cses.fi/problemset/task/1071

A number spiral is an infinite grid whose upper-left square has number 1.
Here are the first five layers of the spiral:

    1   2   9  10  25
    4   3   8  11  24
    5   6   7  12  23
   16  15  14  13  22
   17  18  19  20  21

Your task is to find out the number in row y and column x.

Input :
    The first input line contains an integer t: the number of tests.
    After this, there are t lines, each containing integers y and x.

Output :
    For each test, print the number in row y and column x.

Constraints :
    1 <= t <=10^5
    1 <= y, x <= 10^9

Example :

    Input:
    3
    2 3
    1 1
    4 2

    Output:
    8
    1
    15
"""


def number_spiral(x: int, y: int) -> int:
    """ Решение задачи """

    max_x_y = max(x, y)
    corner_value = max_x_y ** 2 - max_x_y + 1
    x_direction = 1 if max_x_y % 2 == 0 else -1
    y_direction = -1 if max_x_y % 2 == 0 else 1

    return corner_value + x_direction * (abs(max_x_y-x)) + y_direction * (abs(max_x_y-y))


def main() -> None:
    """ Запуск решения """

    tests = int(input())
    for _ in range(tests):
        y, x = map(int, input().split(' '))
        print(number_spiral(x, y))


if __name__ == '__main__':
    main()
