def my_reversed(seq):
    index = len(seq) - 1
    while index >= 0:
        yield seq[index]
        index -= 1


for value in my_reversed([4, 2, 1, 8, 5]):
    print(value)

print()

for char in my_reversed('hello'):
    print(char)
