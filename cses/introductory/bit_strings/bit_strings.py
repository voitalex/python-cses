""" Bit Strings """


def solve(length: int) -> int:
    """ Решение задачи """
    return (2 ** length) % (10 ** 9 + 7)


def main() -> None:
    """ Запуск решения """

    length = int(input())
    print(solve(length))


if __name__ == '__main__':
    main()
