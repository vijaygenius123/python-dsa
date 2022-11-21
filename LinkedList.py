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

    def print(self):
        list_str = ''
        temp = self.head
        while temp:
            list_str += str(temp.value)
            temp = temp.next
            if temp is not None:
                list_str += ' -> '
        print(list_str)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp


if __name__ == '__main__':
    my_linked_list = LinkedList(10)
    my_linked_list.append(9)
    my_linked_list.append(8)
    my_linked_list.append(7)
    my_linked_list.print()
    my_linked_list.pop()
    my_linked_list.pop()
    my_linked_list.print()
    my_linked_list.pop()
    my_linked_list.print()
