"""
Задача-3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def my_func(a, b, c):
    print(f"Сумма наибольших двух аргументов = {a + b + c - min([a, b, c])}")


my_func(int(input("1-й аргумент: ")),
        int(input("2-й аргумент: ")),
        int(input("3-й аргумент: ")))
