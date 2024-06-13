import sys
from collections import deque

input = sys.stdin.readline


def get_primes():
    n = 9999
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            if i > 1000:
                primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


def solve(init, target):
    if init == target:
        return 0

    visited = {i: False for i in primes}
    queue = deque([(init, 0)])
    visited[int(init)] = True
    while queue:
        cur, count = queue.popleft()
        if cur == target:
            return count
        for i in range(4):
            for j in range(10):
                next = cur[:i] + str(j) + cur[i + 1 :]
                if int(next) not in visited or visited[int(next)] == True:
                    continue
                visited[int(next)] = True
                queue.append((next, count + 1))
    return "Impossible"


T = int(input())

primes = get_primes()
for _ in range(T):
    init, target = input().split()
    print(solve(init, target))
