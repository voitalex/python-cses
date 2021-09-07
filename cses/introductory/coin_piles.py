""" Coin Piles

Link: https://cses.fi/problemset/task/1754

You have two coin piles containing a and b coins. On each move, you can either remove one coin from
the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

Input :
    The first input line has an integer t: the number of tests.
    After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output :
    For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints
    1 <= t <= 10^5
    0 <= a, b <= 10^9

Example :

    Input:
    3
    2 1
    2 2
    3 3

    Output:
    YES
    NO
    YES
"""


def coin_piles(first_pile: int, second_pile: int) -> bool:
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
        print('YES' if coin_piles(first_pile, second_pile) else 'NO')


if __name__ == '__main__':
    main()
