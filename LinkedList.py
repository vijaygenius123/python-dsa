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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


if __name__ == '__main__':
    my_linked_list = LinkedList(10)
    my_linked_list.append(9)
    my_linked_list.append(8)
    my_linked_list.append(7)
    my_linked_list.prepend(11)
    print(my_linked_list.get(0).value)
    print(my_linked_list.set(0, 12))
    my_linked_list.insert(1, 11)
    my_linked_list.print()
    my_linked_list.pop()
    my_linked_list.pop()
    my_linked_list.print()
    my_linked_list.pop()
    my_linked_list.insert(3, 9)
    my_linked_list.insert(6, 8)
    my_linked_list.print()
