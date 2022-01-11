from collections import deque
import sys
input = sys.stdin.readline

a = deque([])

order_number = int(input().strip())
count = 0

for i in range(order_number):
    order = input().strip().split()
    if order[0] == "push_front":
        a.appendleft(int(order[1]))
        count += 1

    elif order[0] == "push_back":
        a.append(int(order[1]))
        count += 1

    elif order[0] == "pop_front":
        if count == 0:
            print("-1")
        else:
            print(a.popleft())
            count -= 1

    elif order[0] == "pop_back":
        if count == 0:
            print("-1")
        else:
            print(a.pop())
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
            print(a[0])
    
    elif order[0] == "back":
        if count == 0:
            print("-1")
        else:
            print(a[-1])