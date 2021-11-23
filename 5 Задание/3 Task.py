"""
Задание-3. Создать текстовый файл (не программно), построчно
записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
import sys

work = {"Иванов": 50000, "Петров": 19999, "Сидоров": 40000,
        "Романов": 15500, "Козлов": 40000, "Лесников": 20000}
try:
    file = open("Task3.txt", "w")
    for name, wage in work.items():
        file.write(name + ":" + str(wage) + "\n")
except IOError:
    print("Ошибочные данные.")
    sys.exit()

sum = 0
calc = 0
staff = []
with open("Task3.txt", "r") as file:
    for line in file:
        print(line, end="")
        income = line.split(":")
        if int(income[1]) <= 20000:
            staff.append(income[0])
        sum += int(income[1])
        calc += 1
total = sum / calc
print(f"Сотрудник: {staff}")
print(f"Оклад: {total}")
