class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is self.head and not self.head:
            return
        if node is self.head and not self.head.next_node:
            return
        elif node.next_node:
            if node.next_node:
                next_node = node.get_next()
                node.next_node = prev
                return self.reverse_list(next_node, node)
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
            return
    # runtime of O(n) aka linear time complexity
# sll = LinkedList()
# sll.add_to_head(1)
# sll.add_to_head(2)
# sll.add_to_head(3)
# sll.add_to_head(4)
# sll.add_to_head(5)
# sll.add_to_head(6)
# sll.reverse_list(sll.head, None)
# print(sll.head.get_value())
# print(sll.head.get_next().get_value())
# print(sll.head.get_next().get_next().get_value())
# print(sll.head.get_next().get_next().get_next().get_value())
# print(sll.head.get_next().get_next().get_next().get_next().get_value())
# print(sll.head.get_next().get_next().get_next().get_next().get_next().get_value())

