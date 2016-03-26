# Напишите функцию-генератор, которая будет выдавать
# каждый символ заданной строки count раз
# Пример: repeat_chars('Python', 2) выдаст 'P', 'P',
# 'y', 'y', 't', 't', 'h', 'h', 'o', 'o', 'n', 'n'


def repeat_chars(string, counter):
    for var in range(len(string)):
        for i in range(counter):
            yield string[var]

lst = list(repeat_chars('Python', 6))
print(lst)
