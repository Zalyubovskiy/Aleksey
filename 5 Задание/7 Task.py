"""
7. Создать (не программно) текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой
компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами
и их прибылями, а также словарь со средней прибылью. Если фирма
получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
gain = {}
prof_com = {}
aver_profit = 0
get = 0
x = 0

with open("Task7.txt", 'r', encoding="utf-8") as file:
    for line in file:
        title, ownership, income, costs = line.split()
        gain[title] = int(income) - int(costs)
        if gain.setdefault(title) >= 0:
            get = get + gain.setdefault(title)
            x += 1
    if x != 0:
        aver_profit = get / x
        print(f"Средняя прибыль = {aver_profit}")
    else:
        print("Средняя прибыль меньше прибыли. Убыток.")
    prof_com = {"Средная прибыль": round(aver_profit)}
    gain.update(prof_com)
    print(f"Прибыль каждой компании: {gain}")
with open("Task7.json", 'w', encoding="utf-8") as inner:
    json.dump(gain, inner)
    js_line = json.dumps(gain)
    print(f"Json-файл: \n"
          f"{js_line}")
