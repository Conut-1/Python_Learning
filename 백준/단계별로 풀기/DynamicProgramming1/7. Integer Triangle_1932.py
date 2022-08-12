import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.reverse()
for i in range(n - 1):
    for j in range(n - i - 1):
        arr[i + 1][j] += max(arr[i][j], arr[i][j + 1])

print(arr[n - 1][0])
