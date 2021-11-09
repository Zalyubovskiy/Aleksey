"""
Задача-1.  Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""
import sys


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на ноль")
        sys.exit()
    except ValueError:
        return "Введите число"


print(division(int(input("Введите первое значение: ")),
               int(input("Введите второе значение: "))))
