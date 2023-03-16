def fibonacci(n):
    if n == 0:
        return 0
    cur = 1
    prev = 0
    for _ in range(2, n + 1):
        cur, prev = (cur + prev) % 1_000_000_000, cur
    return cur


N = int(input())

if N == 0:
    print(0)
elif N < 0 and N % 2 == 0:
    print(-1)
else:
    print(1)

print(fibonacci(abs(N)))
