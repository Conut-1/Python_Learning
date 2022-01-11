n = int(input())
postfix = input()
number = []
for i in range(n):
    number.append(input().strip())
stack = []
output = []
for a in postfix:
    if not a in "+-*/":
        stack.append(number[ord(a)-65])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        temp = str(eval(num2 + a + num1))
        stack.append(temp)

# A = 65, Z = 90
print("{:.2f}".format(eval(stack[0])))