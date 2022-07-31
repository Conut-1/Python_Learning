import sys
input = sys.stdin.readline

n = int(input())
arr = input().split()

result = [-1] * n
stack = [0]
dic = {}
for item in arr:
    try:
        dic[item] += 1
    except:
        dic[item] = 1

for i in range(1, n):
    while len(stack) != 0 and dic[arr[stack[-1]]] < dic[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)