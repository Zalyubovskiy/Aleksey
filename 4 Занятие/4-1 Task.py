"""
Задание-1. Реализовать скрипт, в котором должна быть
предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


def calc():
    try:
        work = float(input("Кол-во отработанных часов: "))
        bet = float(input("Рабочая ставка: "))
        bonus = float(input("Премия: "))
        pay = work * bet
        summa = pay + bonus
        print(f"Заработная плата(с премией): {summa}")
    except ValueError:
        print("Ошибочные данные ")
        exit()


calc()


"""
Через argv не получилось:(
from sys import argv

name, work_hour, bet, bonus = argv

calc = (int(work_hour) * int(bet)) + int(bonus)
print(name)
print(work_hour)
print(bet)
print(bonus)
print(f"Ваша з/п: {calc}")
"""