def solve():
    dist = 0
    for i in range(N):
        dist += courses[i]
        if dist > K:
            return i + 1

    for i in range(N - 1, -1, -1):
        dist += courses[i]
        if dist > K:
            return i + 1

N, K = map(int, input().split())
courses = list(map(int, input().split()))

print(solve())
