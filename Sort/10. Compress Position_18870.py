import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sort = sorted(list(set(arr)))

dict = {}
for i in range(len(sort)):
    dict[sort[i]] = i

for i in range(n):
    arr[i] = dict[arr[i]]

print(" ".join(map(str, arr)))
