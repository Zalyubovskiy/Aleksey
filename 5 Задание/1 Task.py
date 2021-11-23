"""
Задание-1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_list = []
while True:
    line = input("Введите любые символы: ")
    if line == "":
        print(new_list)
        exit()
    else:
        newline = line + "\n"
        new_list.append(newline)

    with open("Task1.txt", "w") as file:
        file.writelines(new_list)
