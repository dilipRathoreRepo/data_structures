import collections


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def levelOrderPrint(node):
    if node is None:
        return
    nodes = collections.deque([node])
    current_count, next_count = 1, 0

    while len(nodes) != 0:
        current_node = nodes.popleft()
        print(current_node.key, end=' ')
        current_count -= 1

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1

        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        if current_count == 0:
            print('\n')

            current_count = next_count
            next_count = 0


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left = two
one.right = three

two.left = four
two.right = five

three.left = six
three.right = seven

levelOrderPrint(one)
