"""
Задача-6. Реализовать функцию int_func(), принимающую слово
из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна
попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func().
"""


def int_func(text):
    return text.title()


def title(text):
    word_text = list(text)
    word_text[0] = word_text[0].upper()
    return "".join(word_text)


out_1 = []
out_2 = []
for word in input("Введите нужные слова, через пробел: ").split(" "):
    out_1.append(int_func(word))
    out_2.append(title(word))

print(f"Строка через int_func(text): {' '.join(out_1)}")
print(f"Строка через title: {' '.join(out_2)}")
