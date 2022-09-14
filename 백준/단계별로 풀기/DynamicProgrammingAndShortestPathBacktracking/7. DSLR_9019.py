import sys
from collections import deque
input = sys.stdin.readline


def d(n):
    return (2 * n) % 10000

def s(n):
    return (n + 9999) % 10000

def l(n):
    return (10 * n + n // 1000) % 10000

def r(n):
    return n // 10 + (n % 10) * 1000

def bfs(a, b):
    visited = [0] * 10000
    queue = deque()
    queue.append((a, ""))
    visited[a] = 1
    while queue:
        cur, insts = queue.popleft()
        for inst in ("D", "S", "L", "R"):
            if inst == "D":
                next = d(cur)
                if visited[next] == 1:
                    continue
                queue.append((next, insts + inst))
                visited[next] = 1
            if inst == "S":
                next = s(cur)
                if visited[next] == 1:
                    continue
                queue.append((next, insts + inst))
                visited[next] = 1
            if inst == "L":
                if not insts or insts[-1] != "R" or (len(insts) >= 3 and inst[-3:] != "LLL"):
                    next = l(cur)
                    if visited[next] == 1:
                        continue
                    queue.append((next, insts + inst))
                    visited[next] = 1
            if inst == "R":
                if not insts or insts[-1] != "L" or (len(insts) >= 3 and inst[-3:] != "RRR"):
                    next = r(cur)
                    if visited[next] == 1:
                        continue
                    queue.append((next, insts + inst))
                    visited[next] = 1
            if next == b:
                return insts + inst


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
