"""
Задание-1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен
проводить валидацию числа, месяца и года (например, месяц — от
1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, dd_mm_yy):  # dd_mm_yy - день, месяц, год
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def extract(cls, dd_mm_yy):
        date = []

        for x in dd_mm_yy.split():
            if x != '-':
                date.append(x)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(dd, mm, yy):

        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 2021 >= yy >= 0:
                    return "Верная дата"
                else:
                    return "Неправильный год"
            else:
                return "Неправильный месяц"
        else:
            return "Неправильный день"

    def __str__(self):
        return f"Текущая дата {Data.extract(self.dd_mm_yy)}"


today = Data("25 - 11 - 2010")
print(today)
print(Data.valid(15, 10, 2025))
print(today.valid(12, 13, 2015))
print(Data.extract("25 - 11 - 2010"))
print(today.extract("4 - 4 - 2021"))
print(Data.valid(8, 11, 2004))
