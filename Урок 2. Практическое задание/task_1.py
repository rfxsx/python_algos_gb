"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def recurs_method():
    method_list = ['+', '-', '*', '/']
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '/': lambda x, y: x / y if y != 0 else 'делитель не должен быть 0',
                 '*': lambda x, y: x * y}

    user_method = str(input("Введите операцию (+, -, *, / или 0 для выхода): "))
    if user_method == '0':
        print('Выполнен выход из программы т.к. введен 0')
        exit(1)
    if user_method in method_list:
        try:
            user_first_n = int(input("Введите первое число: "))
            user_second_n = int(input("Введите второе число: "))
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            recurs_method()
        print('Ваш результат: {}'.format(operators[user_method](user_first_n, user_second_n)))
    recurs_method()


recurs_method()
