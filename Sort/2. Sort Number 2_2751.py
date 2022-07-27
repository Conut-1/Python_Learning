import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []
for i in range(n):
    arr.append(int(input().strip()))
for i in sorted(arr):
    print(i)
