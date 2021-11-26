"""
Задание-7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу
проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма = {self.a + other.a} + {self.b + other.b} * n"

    def __mul__(self, other):
        return f"Произведение = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * n"


c_1 = ComplexNumber(5, -48)
c_2 = ComplexNumber(8, 25)
print(c_1 + c_2)
print(c_1 * c_2)


d_1 = ComplexNumber(5, 15)
d_2 = ComplexNumber(8, 22)
print(d_1)
print(d_1 + d_2)
print(d_1 * d_2)
