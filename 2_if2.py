"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    first_row = input('Введите первую строку:')
    second_row = input('Введите вторую строку:')
    if first_row == str and second_row == str:
        return 0
    elif first_row == second_row:
        return 1
    elif first_row != second_row and len(first_row) > len(second_row):
        return 2
    elif first_row != second_row and second_row == 'learn':
        return 3
    else:
        return 4


print(main())
