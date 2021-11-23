"""
Задание-4. Реализуйте базовый класс Car. У данного класса
должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые
должны сообщать, что машина поехала, остановилась, повернула
(куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"А/м {self.name} поехал\n."

    def stop(self):
        return f"А/м {self.name} становился.\n"

    def turn(self, direction):
        return f"А/м {self.name} повернул {direction}.\n"

    def show_speed(self):
        return f"Текущая скорость а/м: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nСкорость а/м: {self.speed}- превышении скорости."
        else:
            return f"Скорость а/м {self.name}: {self.speed}."


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nСкорость а/м: {self.speed}- превышении скорости."
        else:
            return f"Скорость а/м {self.name}: {self.speed}."


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar("Reno Duster", 80, "Чёрный", False)
print("1:\n" + town.go(), town.show_speed(), town.turn("Вправо"), town.stop())

work = WorkCar("УАЗ-452", 40, "Белый", False)
print("2:\n" + work.go(), work.show_speed(), work.turn("Влево"), work.stop())

sport = SportCar("Ferrari-812", 170, "Красный", False)
print("3:\n" + sport.go(), sport.show_speed(), sport.turn("Вправо"), sport.stop())

police = PoliceCar("Лада-Веста", 100, "Белый", True)
print("4:\n" + police.go(), police.show_speed(), police.turn("Вправо"), police.stop())
