import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    cur = int(input())
    if cur == 0:
       arr.pop()
    else:
        arr.append(cur)

print(sum(arr))
