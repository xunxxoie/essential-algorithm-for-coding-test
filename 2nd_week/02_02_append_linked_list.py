class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        result = ""

        while cur is not None:
            result = result + "[" + str(cur.data) + "]" + "->"
            cur = cur.next

        print(result)

node = Node(5)

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.print_all()