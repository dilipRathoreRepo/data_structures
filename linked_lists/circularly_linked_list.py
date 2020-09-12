class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


n1 = SinglyLinkedList(1)
n2 = SinglyLinkedList(2)
n3 = SinglyLinkedList(3)

n1.next_node = n2
n2.next_node = n3
n3.next_node = n1


def check_cycle(node):
    original_node = node
    nxt_node = node.next_node
    while True:
        if nxt_node.next_node is None:
            return False
        elif nxt_node is original_node:
            return True
        nxt_node = nxt_node.next_node


print(check_cycle(n1))
