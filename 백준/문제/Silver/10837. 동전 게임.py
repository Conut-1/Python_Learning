import sys

input = sys.stdin.readline

K = int(input())
C = int(input())
for _ in range(C):
    M, N = map(int, input().split())

    if M > N:
        if M <= N + K - max(M, N) + 2:
            print(1)
        else:
            print(0)
    elif M < N:
        if M + K - max(M, N) + 1 >= N:
            print(1)
        else:
            print(0)
    else:
        print(1)
