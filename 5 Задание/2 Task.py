"""
Задание-2. Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
new_list = ["Приветствую\n",
            "вас\n",
            "в\n",
            "данном\n",
            "практическом\n",
            "задании!\n"]
with open("Task2.txt", "w+") as file:
    file.writelines(new_list)
with open("Task2.txt") as file:
    line = 0
    word_line = 0
    for lines in file:
        line += lines.count("\n")
        word_line = len(lines) - 1
        print(f"{word_line} - слов в строке.")
    print(f"{line} - кол-во строк.")
