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
        if not self.isEmpty():
            pop_object = self.head.data
            self.head = self.head.next
        return pop_object

    def top(self):
        top_object = None
        if not self.isEmpty():
            top_object = self.head.data
        return top_object

    def isEmpty(self):
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty

sequence = []
calculation = []
count = 1
stack = LinkedListStack()
order_number = int(input())
for i in range(order_number):
    sequence.append(int(input()))

for i in range(order_number):
    while sequence[i] >= count:
        stack.push(count)
        calculation.append("+")
        count += 1
    if sequence[i] == stack.top():
        stack.pop()
        calculation.append("-")
    else:
        print("NO")
        break
    if i == order_number - 1:
        for i in range(len(calculation)):
            print(calculation[i])