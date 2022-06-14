class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if not new_node:
            return "some error occured"

        #push on empty stack
        if self.head == None:
            self.head = new_node
        else:
            # push when item already present on stack
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return "Stack is empty"
        el = self.head.data
        self.head = self.head.next
        return el


# Driver code
tabs = Stack()
tabs.push(1)
tabs.push(2)
tabs.push(7)
el = tabs.pop()
print(el)
el = tabs.pop()
print(el)
e = tabs.push(10)
el = tabs.pop()
print(el)
el = tabs.pop()
print(el)
el = tabs.pop()
print(el)
