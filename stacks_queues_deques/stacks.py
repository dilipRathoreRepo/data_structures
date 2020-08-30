"""
An ordered collections of items where addition and removal always happens at one end.
This end is referred as top. The other end is known as base. (e.g. stack of books on a table)
works on LIFO principle.
"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        k = len(self.stack) - 1
        return self.stack.pop(k)

    def peek(self):
        k = len(self.stack) - 1
        return self.__getitem__(k)

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, k):
        if 0 <= k < len(self.stack):
            return self.stack[k]
        return IndexError(f'Index {k} is out of bounds!')

    def __str__(self):
        stack_str = ','.join(map(str, self.stack))
        return stack_str


if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    print(s.isEmpty())
    print(s.size())

    print(f'Length of s is {len(s)}')
    print(s)
    print(s.peek())

    s.push('a')
    s.push(2)
    print(f'Length of s is {len(s)}')
    print(s)
    print(s.peek())

    s.pop()
    print(f'Length of s is {len(s)}')
    print(s)
    print(s.peek())

    print(s[0])
    print(s[1])
