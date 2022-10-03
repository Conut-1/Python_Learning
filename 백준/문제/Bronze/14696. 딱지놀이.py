import sys
input = sys.stdin.readline


def solve(a, b):
    for i in range(4, 0, -1):
        if a[i] > b[i]:
            return "A"
        if a[i] < b[i]:
            return "B"
    return "D"

N = int(input())
for _ in range(N):
    a_input = list(map(int, input().split()))
    b_input = list(map(int, input().split()))
    a = [0] * 5
    b = [0] * 5
    for shape in a_input[1:]:
        a[shape] += 1
    for shape in b_input[1:]:
        b[shape] += 1
    print(solve(a, b))
