import sys
input=sys.stdin.readline

input_str = list(input().strip())
stack = []
order_number = int(input().strip())
for i in range(order_number):
    order = input().strip().split()
    if order[0] == "L":
        if input_str:
            stack.append(input_str.pop())
    elif order[0] == "D":
        if stack:
            input_str.append(stack.pop())
    elif order[0] == "B":
        if input_str:
            input_str.pop()
    else:
        input_str.append(order[1])

while stack:
    input_str.append(stack.pop())

print("".join(input_str))