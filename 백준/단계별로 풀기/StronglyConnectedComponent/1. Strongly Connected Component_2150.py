import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V, E = map(int, input().split())

def find_scc(i):
    global id

    id += 1
    visited[i] = id
    stack.append(i)

    result = visited[i]
    for next in graph[i]:
        if visited[next] == 0:
            result = min(result, find_scc(next))
        elif not finished[next]:
            result = min(result, visited[next])

    if result == visited[i]:
        cur_scc = []
        while True:
            t = stack.pop()
            cur_scc.append(t)
            finished[t] = 1
            if t == i:
                break
        cur_scc.sort()
        scc.append(cur_scc)

    return result

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

id = 0
scc = []
stack = []
visited = [0] * (V + 1)
finished = [0] * (V + 1)
for i in range(1, V + 1):
    if visited[i] == 0:
        find_scc(i)

scc.sort()
print(len(scc))
for cur_scc in scc:
    print(*cur_scc, -1)
