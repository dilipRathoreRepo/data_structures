
class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    # def __str__(self):
    #     return self.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)


a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f


# OPTION 1 (My solution):
# def nth_to_last_node(n, node):
#     bag = [node]
#     while node is not None:
#         node = node.nextnode
#         bag.append(node)
#     bag = bag[::-1]
#     return bag[n].value

# OPTION 2
def nth_to_last_node(n, node):
    """
    Create two pointers. Move right pointer ahead as many number of times as 'n' so that left pointer is always 'n'
    positions behind the right pointer.. Then move both pointers ahead one step a time until right pointer's nextnode
    is None. Then return the left node.
    :param n:
    :param node:
    :return:
    """
    left_pointer = node
    right_pointer = node

    for i in range(n-1):
        if right_pointer.nextnode is None:
            raise LookupError('Not enough nodes in linked list')
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode is not None:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer.value


print(nth_to_last_node(3, a))
