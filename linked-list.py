class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def create_list(num):
    if num < 1:
        return None
    head = Node(1)
    current = head
    for i in range(2, num+1):
        # Create a new Node with value and point next of current to this
        current.next = Node(i)

        # Increment the current to point to newlly created node
        current = current.next
    return head

def traverse_list(head):
    if head == None:
        return None
    current = head
    while(current):
        print("data value is", current.data)
        current = current.next

def delete_first_node(head):

    return head

h = create_list(10)
traverse_list(h)
