class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return None
        else:
            pop_node = self.head
            self.head = pop_node.next
            return pop_node

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()

stack.push(10)
stack.push(11)
stack.push(12)

print(stack.peek())

stack.pop()
stack.pop()
stack.pop()

print(stack.peek() )