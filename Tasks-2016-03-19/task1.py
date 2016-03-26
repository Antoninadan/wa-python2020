# Напишите функцию-генератор, которая будет выдавать
# числа в диапазоне от нуля до заданного числа
# (как range с одним параметром)

def my_range(limit):
    for i in range(limit):
        yield i

list = list(my_range(90))
print(list)