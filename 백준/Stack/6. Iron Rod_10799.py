input_value = input()
count = 0
stack = []
laser = 0
result = 0
for i in input_value:
    stack.append(i)

while stack:
    if stack.pop() == ")":
        count += 1
        if laser == 1:
            laser = 0
    else:
        count -= 1
        if laser == 0:
            laser = 1
            result += count
        else:
            result += 1

print(result)