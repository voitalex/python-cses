""" Coin Piles """


def solve(first_pile: int, second_pile: int) -> bool:
    """ Решение задачи """

    if first_pile == 0 and second_pile == 0:
        return True

    if (first_pile + second_pile) % 3 > 0:
        return False

    moves = (first_pile + second_pile) // 3

    return first_pile > 0 and second_pile > 0 and (0 < moves <= min(first_pile, second_pile))


def main() -> None:
    """ Запуск решения """

    tests = int(input())
    for _ in range(tests):
        first_pile, second_pile = map(int, input().split(' '))
        print('YES' if solve(first_pile, second_pile) else 'NO')


if __name__ == '__main__':
    main()
