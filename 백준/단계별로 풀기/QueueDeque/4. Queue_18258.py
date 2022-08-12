import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.__num = num
        self.next = None

    def print_num(self):
        print(self.__num)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.__size = 0

    def push(self, num):
        if self.__size == 0:
            self.first = Node(num)
            self.last = self.first
        else:
            self.last.next = Node(num)
            self.last = self.last.next
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            print(-1)
            return
        temp = self.first
        self.first = self.first.next
        temp.print_num()
        del temp
        self.__size -= 1
        if self.__size == 0:
            self.last = None

    def size(self):
        print(self.__size)

    def empty(self):
        if self.__size == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.__size == 0:
            print(-1)
        else:
            self.first.print_num()

    def back(self):
        if self.__size == 0:
            print(-1)
        else:
            self.last.print_num()

n = int(input())

queue = Queue()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "empty":
        queue.empty()
    elif command[0] == "front":
        queue.front()
    elif command[0] == "back":
        queue.back()
