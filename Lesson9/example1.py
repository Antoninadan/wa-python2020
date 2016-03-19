class MyReversed:
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)
        self.next_index = self.length - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_index < 0:
            raise StopIteration
        value = self.seq[self.next_index]
        self.next_index -= 1
        return value


for x in MyReversed([1, 5, 2, 18]):
    print(x)

print()

for x in MyReversed('hello'):
    print(x)
