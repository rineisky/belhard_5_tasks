"""
Функция get_score возвращает оценку за контрольную работу

в if __name__ == '__main__': описать следующее:

в блоке try:
- получить значение get_score()
- если значение меньше 7, то кинуть ошибку ValueError со значением оценки
- вывести на экран сообщение 'Ребенок получил хорошую оценку'
- записать в переменную gift результат random_gift()

В блоке обработки RuntimeError:
- вывести сообщение об ошибке на экран
- вызвать функцию punish_dog()

В блоке обработки ValueError:
- вызвать функцию punish_child и передать в нее полученную ошибку

В блоке else:
- вызвать функцию praise и передать в нее значение gift

В блоке finally:
- вызвать функцию cook_dinner
"""
import random


def get_score():
    result = random.randint(-5, 10)
    if result <= 0:
        raise RuntimeError('Собака съела дневник')
    return result


def punish_child(bad_score):
    print(f'Всыпать ремня за то, что ребенок получил {bad_score}')


def punish_dog():
    print('Накричать на собаку')


def praise(some_gift):
    print(f'Дать денежку на: {some_gift}')


def cook_dinner():
    print('\nПриготовить ужин')


def random_gift():
    return random.choice(['мороженое', 'сникерс', 'чипсы'])


if __name__ == '__main__':
    print("Просим показать ребенка дневник\n")
    gift = None
    # TODO написать свой код здесь
