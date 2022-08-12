s = input()
check = 0
stack = []
result = ''

for i in range(len(s)):
    if check == 0:
        if s[i] != '<' and s[i] != ' ':
            stack.append(s[i])
        else:
            while(len(stack)):
                result += stack.pop()
            result += s[i]
            if(s[i] == '<'):
                check = 1
    else:
        result += s[i]
        if s[i] == '>':
            check = 0

while(len(stack)):
    result += stack.pop()
print(result)