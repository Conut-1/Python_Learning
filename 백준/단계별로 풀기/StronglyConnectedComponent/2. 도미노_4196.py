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

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    id = 0
    scc_id = 0
    scc = []
    stack = []
    visited = [0] * (V + 1)
    finished = [-1] * (V + 1)
    for i in range(1, V + 1):
        if visited[i] == 0:
            find_scc(i)

    scc_graph = [set() for _ in range(len(scc))]
    in_degree = [0] * len(scc)
    for i in range(len(scc)):
        for node in scc[i]:
            for next in graph[node]:
                if finished[node] != finished[next]:
                    in_degree[finished[next]] += 1

    count = 0
    for i in range(len(scc)):
        if in_degree[i] == 0:
            count += 1

    print(count)
