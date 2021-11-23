"""
Задание-4. Создать (не программно) текстовый файл со следующим
содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

num_list = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
some_list = []
total = []

try:
    file_out = open("Task4_out.txt", "r", encoding="utf-8")
    for line in file_out:
        num = line.split(" - ")
        print(num)
        if num[0] in num_list:
            fig = num_list[num[0]]
            total.append(fig + ' - ' + num[1])
    print(total)
except IOError:
    print("Ошибочные данные.")
finally:
    file_out.close()

try:
    file_in = open("Task4_in.txt", 'w', encoding="utf-8")
    file_in.writelines(total)
except IOError:
    print("Ошибочные данные.")
finally:
    file_in.close()
