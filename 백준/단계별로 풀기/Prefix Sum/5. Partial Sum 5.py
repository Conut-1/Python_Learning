import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [[0] * (n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    arr.append([0])
    for j in range(1, n + 1):
        arr[i].append(temp[j - 1] + arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1])

for i in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    print(arr[x_2][y_2] - arr[x_1 - 1][y_2] - arr[x_2][y_1 - 1] + arr[x_1 - 1][y_1 - 1])
