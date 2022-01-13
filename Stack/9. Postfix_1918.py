input_value = input()
stack = []
output = ""

for a in input_value:
    if a in "*/":
        if stack and (stack[-1] in "*/"):
            output += stack.pop()
        stack.append(a)
    elif a in "+-":
        while stack:
            if stack[-1] == "(":
                break
            output += stack.pop()
        stack.append(a)
    elif a in "(":
        stack.append(a)
    elif a in ")":
        while stack[-1] != "(":
            output += stack.pop()
        stack.pop()
    else:
        output += a

while stack:
    output += stack.pop()

print(output)