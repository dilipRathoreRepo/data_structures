class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.nextnode = n2
n2.nextnode = n3
n3.nextnode = n4

# print(n1.nextnode.value)
# print(n2.nextnode.value)
# print(n3.nextnode.value)
# print(n4.nextnode.value)


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return previous


print(reverse(n1))

print(n4.nextnode.value)
print(n3.nextnode.value)
print(n2.nextnode.value)
# print(n1.nextnode.value)
