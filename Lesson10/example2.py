def generator1():
    yield 1
    yield 2
    yield 3

for x in generator1():
    print(x)


def generator2():
    yield 'before'
    yield from generator1()
    yield 'after'

print(list(generator2()))


def generator3():
    yield from range(5)

print(list(generator3()))
