""" Number Spiral """


def solve(x: int, y: int) -> int:
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
        print(solve(x, y))


if __name__ == '__main__':
    main()
