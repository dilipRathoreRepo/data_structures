"""
It is also known as double ended queue. It is ordered collection. It has two ends, front and rear.
New items can be added either at front or rear.
"""


class Deque(object):
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.append(item)

    def removeFront(self):
        self.deque.pop()

    def addRear(self, item):
        k = 0
        self.deque.insert(k, item)

    def removeRear(self):
        k = 0
        self.deque.pop(k)

    def isEmpty(self):
        return len(self.deque) == 0

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.deque)

    def __getitem__(self, k):
        if 0 <= k < len(self.deque):
            return self.deque[k]
        return IndexError(f'Index {k} is out of bounds!')

    def __str__(self):
        stack_str = ','.join(map(str, self.deque))
        return stack_str


d = Deque()
print(d.isEmpty())
d.addRear(1)
d.addRear(2)
d.addRear(3)
print(f'Length of d is {len(d)}')
print(d)

d.removeRear()
print(f'Length of d is {len(d)}')
print(d)

d.removeFront()
print(f'Length of d is {len(d)}')
print(d)

d.addFront(4)
print(f'Length of d is {len(d)}')
print(d)
