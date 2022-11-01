string = input()
explode = input()

stack = []
tmp = []
for char in string:
    stack.append(char)
    i = len(explode) - 1
    while stack and i >= 0 and stack[-1] == explode[i]:
        tmp.append(stack.pop())
        i -= 1
    if len(tmp) == len(explode):
        while tmp:
            tmp.pop()
    else:
        while tmp:
            stack.append(tmp.pop())

if len(stack):
    print("".join(stack))
else:
    print("FRULA")
