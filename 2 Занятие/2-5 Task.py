"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
"""
num = int(input("Введите число: "))
my_list = [8, 6, 2]
a = my_list.count(num)
for count in my_list:
    if a > 0:
        b = my_list.index(num)
        my_list.insert(b+a, num)
        break
    else:
        if num > count:
            c = my_list.index(count)
            my_list.insert(c, num)
            break
        elif num <= my_list[len(my_list)-1]:
            my_list.append(num)
print(my_list)