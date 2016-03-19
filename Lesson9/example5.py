class Node:
    __slots__ = ('value', 'next')

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class List:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0
        if iterable is not None:
            self.extend(iterable)

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def __getitem__(self, index):
        if index < 0:
            index += self.length
        if index >= self.length:
            raise IndexError(index)
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value

    def __len__(self):
        return self.length

    def __repr__(self):
        return 'List([' + ', '.join(map(repr, self)) + '])'

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next


lst = List(range(10000))
print(lst)
