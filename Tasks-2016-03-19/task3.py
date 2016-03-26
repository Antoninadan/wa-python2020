# Напишите функцию-генератор count первых чисел Фибоначчи


def fibonacci(count):
    prev, last = 0, 1
    for i in range(count):
        yield last;
        prev, last = last, prev + last

for i in fibonacci(5): print(i)
