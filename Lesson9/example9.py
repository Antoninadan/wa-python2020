# Generator expression
pairs = ((x, y) for x in range(5) for y in range(3) if x != y)
pairs_list = list(pairs)
print(pairs_list)


# Generator
def generator():
    for x in range(5):
        for y in range(3):
            if x != y:
                yield (x, y)
pairs = generator()
pairs_list = list(pairs)
print(pairs_list)


# Imperative loop
pairs_list = []
for x in range(5):
    for y in range(3):
        if x != y:
            pairs_list.append((x, y))
print(pairs_list)
