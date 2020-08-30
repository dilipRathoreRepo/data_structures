"""
A queue is an ordered collection of items where addition of items happens at rear and removal happens from front.
It works on FIFO principle
Enqueue means adding item at the rear. Dequeue means removing item from front
"""


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        k = 0
        self.queue.pop(k)

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, k):
        if 0 <= k < len(self.queue):
            return self.queue[k]
        return IndexError(f'Index {k} is out of bounds!')

    def __str__(self):
        stack_str = ','.join(map(str, self.queue))
        return stack_str


q = Queue()
print(q.isEmpty())
q.enqueue(1)
print(q.isEmpty())
print(q.size())

print(f'Length of q is {len(q)}')
print(q)

q.enqueue('a')
q.enqueue(2)
print(f'Length of q is {len(q)}')
print(q)

q.dequeue()
print(f'Length of q is {len(q)}')
print(q)

print(q[0])
print(q[1])
