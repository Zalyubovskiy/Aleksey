"""
Задание-5. Создать (программно) текстовый файл, записать в
него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summa():
    try:
        with open("Task5.txt", 'w') as file:
            line = input("Введите цифры, через пробел: \n")
            file.writelines(line)
            num = line.split()
            print(sum(map(int, num)))
    except IOError:
        print("Ошибка")
    except ValueError:
        print("Ошибка ввода-вывода")


summa()
