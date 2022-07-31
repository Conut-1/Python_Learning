from collections import deque
import sys
input = sys.stdin.readline
queue = deque([])

order_number = int(input().strip())
count = 0

for i in range(order_number):
    order = input().strip().split()
    if order[0] == "push":
        queue.append(int(order[1]))
        count += 1

    elif order[0] == "pop":
        if count == 0:
            print("-1")
        else:
            print(queue.popleft())
            count -= 1

    elif order[0] == "size":
        print(count)

    elif order[0] == "empty":
        if count == 0:
            print("1")
        else:
            print("0")

    elif order[0] == "front":
        if count == 0:
            print("-1")
        else:
            print(queue[0])
    
    elif order[0] == "back":
        if count == 0:
            print("-1")
        else:
            print(queue[-1])