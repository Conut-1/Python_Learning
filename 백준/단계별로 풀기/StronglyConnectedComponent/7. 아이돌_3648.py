import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

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

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    graph = [[] for _ in range(2 * n + 1)]
    graph[-1].append(1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[-a].append(b)
        graph[-b].append(a)

    id = 0
    scc_id = 0
    scc = []
    stack = []
    visited = [0] * (2 * n + 1)
    finished = [-1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        if visited[i] == 0:
            find_scc(i)

    for i in range(1, n + 1):
        if finished[i] == finished[-i]:
            print("no")
            break
    else:
        print("yes")
