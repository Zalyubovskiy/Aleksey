"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
import sys

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
num_month = int(input("Введите номер месяца(1-12): "))
seas_list = 0
seas_dict = 1
if num_month in (1, 2, 12):
    seas_list = seasons_list[0]
    seas_dict = seasons_dict.get(1)
elif num_month in (3, 4, 5):
    seas_list = seasons_list[1]
    seas_dict = seasons_dict.get(2)
elif num_month in (6, 7, 8):
    seas_list = seasons_list[2]
    seas_dict = seasons_dict.get(3)
elif num_month in (9, 10, 11):
    seas_list = seasons_list[3]
    seas_dict = seasons_dict.get(4)
else:
    print('Неверно задан месяц.')
    sys.exit()
print(f"Сезон(list): {seas_list},\nСезон(dict): {seas_dict}")
