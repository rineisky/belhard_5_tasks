"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""

from collections import Counter


def common_and_longest(text: str) -> tuple:
    words = text.split(' ')
    count = Counter(words)
    common = count.most_common(1)[0][0]
    longest = words[0]
    for i in count.keys():
        if len(i) > len(longest):
            longest = i
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
