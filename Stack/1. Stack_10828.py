import sys

input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def get_order_number(self):
        number = int(input().strip())

        for i in range(number):
            order = input().strip()
            if "push" in order:
                a = order.split(" ")
                data_number = int(a[1])
                self.push(data_number)
            elif order == "pop":
                print(self.pop())
            elif order == "top":
                print(self.top())
            elif order == "size":
                print(self.size())
            else:
                print(self.empty())

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = -1
        if not self.empty():
            pop_object = self.stack.pop()

        return pop_object

    def top(self):
        top_object = -1
        if not self.empty():
            top_object = self.stack[-1]            

        return top_object

    def empty(self):
        is_empty = 1
        if len(self.stack):
            is_empty = 0
        
        return is_empty

    def size(self):
        return len(self.stack)

stack = Stack()
stack.get_order_number()