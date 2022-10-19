def solve(n):
    if n == 0:
        return
    for i in range(2 * N - 2 * n, 2 * N + 2 * n - 3):
        arr[2 * N - 2 * n][i] = "*"
    for i in range(2 * N - 2 * n, 2 * N + 2 * n - 1):
        arr[i][2 * N - 2 * n] = "*"
    for i in range(2 * N - 2 * n, 2 * N + 2 * n - 3):
        arr[2 * N + 2 * n - 2][i] = "*"
    for i in range(2 * N - 2 * n + 2, 2 * N + 2 * n - 1):
        arr[i][2 * N + 2 * n - 4] = "*"
    if n > 1:
        arr[2 * N - 2 * n + 2][2 * N + 2 * n - 5] = "*"
    solve(n - 1)

N = int(input())

arr = [[" "] * (4 * (N - 1) + 1) for _ in range(4 * N - 1)]
if N == 1:
    print("*")
else:
    solve(N)
    for line in arr:
        print("".join(line).strip())
