class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


n1 = DoublyLinkedList(1)
n2 = DoublyLinkedList(2)
n3 = DoublyLinkedList(3)

n1.next_node = n2
n2.prev_node = n1

n2.next_node = n3
n3.prev_node = n2

