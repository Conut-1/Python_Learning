import sys
input = sys.stdin.readline

while True:
    str = input().rstrip()
    if str == ".":
        break
    flag = 0
    stack = []
    for c in str:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0 or stack.pop() != "(":
                flag = 1
                print("no")
                break
        elif c == "]":
            if len(stack) == 0 or stack.pop() != "[":
                flag = 1
                print("no")
                break

    if flag == 0:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")
