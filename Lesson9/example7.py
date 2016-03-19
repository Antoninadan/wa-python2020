def squared_seq(seq):
    for value in seq:
        yield value ** 2


values = [1, 2, 3, 4, 5]

for square in squared_seq(values):
    print(square)

print()

for square in (x ** 2 for x in values):
    print(square)
