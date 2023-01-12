def solve():
    for i in range(L, 100 + 1):
        t = i * (i - 1) // 2
        if (N - t) % i == 0:
            x = (N - t) // i
            if x >= 0:
                print(*[x + j for j in range(i)])
                return
    print(-1)
    return

N, L = map(int, input().split())

solve()
