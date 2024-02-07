import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

res = -1
for i in range(n - 2):
    a, b, c = arr[len(arr) - i - 3], arr[len(arr) - i - 2], arr[len(arr) - i - 1]
    if a + b > c:
        res = a + b + c
        break

print(res)
