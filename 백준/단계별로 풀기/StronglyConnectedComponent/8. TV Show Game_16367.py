from itertools import combinations
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

TRUE = "B"
FALSE = "R"

def find_scc(i):
    global id
    global scc_id

    id += 1
    visited[i] = id
    stack.append(i)

    result = visited[i]
    for next in graph[i]:
        if visited[next] == 0:
            result = min(result, find_scc(next))
        elif finished[next] == -1:
            result = min(result, visited[next])

    if result == visited[i]:
        cur_scc = []
        while True:
            t = stack.pop()
            cur_scc.append(t)
            finished[t] = scc_id
            if t == i:
                break
        scc.append(cur_scc)
        scc_id += 1

    return result

k, n = map(int, input().split())

graph = [[] for _ in range(2 * k + 1)]
for _ in range(n):
    guess = input().split()
    a = int(guess[0]) if guess[1] == TRUE else -int(guess[0])
    b = int(guess[2]) if guess[3] == TRUE else -int(guess[2])
    c = int(guess[4]) if guess[5] == TRUE else -int(guess[4])
    for x, y in combinations([a, b, c], 2):
        graph[-y].append(x)
        graph[-x].append(y)

id = 0
scc_id = 0
scc = []
stack = []
visited = [0] * (2 * k + 1)
finished = [-1] * (2 * k + 1)
for i in range(1, 2 * k + 1):
    if visited[i] == 0:
        find_scc(i)

result = ""
for i in range(1, k + 1):
    if finished[i] == finished[-i]:
        print(-1)
        break
    if finished[i] < finished[-i]:
        result += TRUE
    else:
        result += FALSE
else:
    print(result)
