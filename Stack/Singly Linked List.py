class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack():
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empyt")
        else:
            pop_object = self.head.data
            self.head = self.head.next
        return pop_object

    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.head.data
        return top_object

    def isEmpty(self):
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty