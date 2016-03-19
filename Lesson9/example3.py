values = [5, 2, 1, 8, 3]

# for value in values:
#     print(value)

it = iter(values)
try:
    while True:
        value = next(it)
        # loop body start
        print(value)
        # loop body end
except StopIteration:
    pass
