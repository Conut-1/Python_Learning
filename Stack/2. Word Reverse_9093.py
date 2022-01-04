class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if not self.empty():
            pop_object = self.stack.pop()

        return pop_object

    def empty(self):
        is_empty = True
        if len(self.stack):
            is_empty = False
        
        return is_empty

class Reverse(Stack):
    def __init__(self):
        self.stack = Stack()
        self.word = []
        self.order_number = 0

    def get_order_number(self):
        self.order_number = int(input())

    def get_sentence(self):
        self.word.extend(input().split(" "))

    def word_reverse(self):
        for i in range(len(self.word)):
            for j in range(len(self.word[i])):
                self.stack.push(self.word[i][j])
            for j in range(len(self.word[i])):
                temp = list(self.word[i])
                temp[j] = self.stack.pop()
                self.word[i] = "".join(temp)

    def clear_sentence(self):
        self.word.clear()

reverse = Reverse()
reverse.get_order_number()
for i in range(reverse.order_number):
    reverse.get_sentence()
    reverse.word_reverse()
    print(" ".join(reverse.word))
    reverse.clear_sentence()