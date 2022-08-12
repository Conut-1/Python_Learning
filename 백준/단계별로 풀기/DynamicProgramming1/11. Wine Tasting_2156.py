import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr2 = [[arr[0], arr[0], arr[0], 0, 0]]
for i in range(1, n):
    arr2.append([arr[i] + max(arr2[i - 1][1], arr2[i - 1][2]), arr[i] + arr2[i - 1][3], arr[i] + arr2[i - 1][4], max(arr2[i - 1][0], arr2[i - 1][1], arr2[i - 1][2]), arr2[i - 1][3]])
    
print(max(arr2[n - 1]))
