import sys
input = sys.stdin.readline


def solve():
    i = 0
    while i < N - 1:
        if arr[i] < arr[i + 1]:
            i += 1
        else:
            break
    while i < N - 1:
        if arr[i] > arr[i + 1]:
            i += 1
        else:
            return "NO"
    return "YES"


N = int(input())
arr = list(map(int, input().split()))

print(solve())
