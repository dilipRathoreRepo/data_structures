
# class Queue2Stacks(object):
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self, item):
#         self.stack1.append(item)
#
#     def dequeue(self):
#         length = len(self.stack1)
#         if length == 0:
#             raise IndexError(f'No more elements left')
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#         output = self.stack2.pop()
#         self.stack1 = list(reversed(self.stack2))
#         self.stack2 = []
#         return output
#
#     def __str__(self):
#         return ','.join(map(str, self.stack1))


class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):

        # Add an enqueue with the "IN" stack
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def __str__(self):
        return ','.join(map(str, self.instack))


# q = Queue2Stacks()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# q.dequeue()  # Removes 1
# print(q)
# q.dequeue()  # Removes 2
# print(q)
# q.dequeue()  # Removes 3
# print(q)
# # q.dequeue()  # IndexError
# # print(q)
# q.enqueue('a')
# print(q)
# q.enqueue('b')
# print(q)
# q.dequeue()
# print(q)

q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
