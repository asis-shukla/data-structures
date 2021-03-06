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
    print("********* Traverse complete ************")


def delete_first_node(head):
    # Check for null linked list
    if head == None:
        return None
    head = head.next
    return head


def delete_value_node(head, value):
    if head == None:
        return None
    current = head
    while(current.next and current.next.data != value ):
        current = current.next
    if current.next:
        current.next = current.next.next
    return head


def delete_last_node(head):
    if head == None:
        return None
    current = head

    # Traverse till last - 1 node to remove last node
    while(current.next.next != None):
        current = current.next
    current.next = None
    return head


h = create_list(10)
traverse_list(h)
h = delete_first_node(h)
traverse_list(h)
h = delete_last_node(h)
traverse_list(h)
h = delete_value_node(h, 11)
traverse_list(h)
