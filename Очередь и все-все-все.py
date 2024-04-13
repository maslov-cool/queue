class Queue:
    def __init__(self, *args):
        self.lst = list(args)

    def append(self, *values):
        self.lst += values

    def copy(self):
        return Queue(*self.lst)

    def pop(self):
        if self.lst:
            el = self.lst[0]
            del self.lst[0]
            return el
        return

    def extend(self, queue):
        self.lst += queue.lst

    def next(self):
        return Queue(*self.lst[1:])

    def __add__(self, other):
        return Queue(*(self.lst + other.lst))

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.lst == other.lst

    def __rshift__(self, other):
        return Queue(*self.lst[other:])

    def __str__(self):
        return '[' + ' -> '.join(str(i) for i in self.lst) + ']' if self.lst else '[]'

    def __next__(self):
        return Queue(*self.lst[1:])







