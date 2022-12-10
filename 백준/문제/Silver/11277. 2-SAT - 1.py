import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solve():
    for i, j in clauses:
        if ((x[i] if i > 0 else not x[-i]) or (x[j] if j > 0 else not x[-j])) == False:
            return False
    return True

def dfs(n):
    if n == N + 1:
        if solve() == True:
            print(1)
            exit(0)
        return
    dfs(n + 1)
    x[n] = False
    dfs(n + 1)
    x[n] = True

N, M = map(int, input().split())

x = [True] * (N + 1)
clauses = [list(map(int, input().split())) for _ in range(M)]

dfs(1)
print(0)
