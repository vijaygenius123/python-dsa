class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


if __name__ == '__main__':
    my_linked_list = LinkedList(10)
    print(my_linked_list.head.value)
