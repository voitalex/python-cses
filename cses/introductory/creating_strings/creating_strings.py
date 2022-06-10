""" Creating Strings """

from typing import Iterable, List


def solve(string: str) -> Iterable[str]:
    """ Решение задачи """

    size = len(string)
    items = sorted(string)

    def _solve(items: List[str]):

        while True:

            # Возвращаем найденную последовательность
            yield ''.join(items)

            # Находим начало самой длинной невозрастающей последовательности символов с конца строки
            # items[i] < items[i + 1]
            for i in range(size - 2, -1, -1):
                if items[i] < items[i + 1]:
                    break
            # Если начало таковой последовательности не найдено, то текущая перестановка является последней
            else:
                return

            # Находим первый элемент от конца последовательности, который превышает
            # начало невозрастающей последовательности
            for j in range(size - 1, i, -1):
                if items[i] < items[j]:
                    break

            # Меняем местами элементы items[i] и items[j]
            # и переворачиваем последовательность элементов, начиная с items[i + 1]
            items[i], items[j] = items[j], items[i]
            items[i + 1:] = items[:i - size: -1]

    yield from _solve(items)


def main():
    """ Запуск решения """

    string = input()
    permutations = list(solve(string))

    print(len(permutations))
    for permutation in permutations:
        print(permutation)


if __name__ == '__main__':
    main()
