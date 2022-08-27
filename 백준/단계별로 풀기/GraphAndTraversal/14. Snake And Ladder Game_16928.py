from collections import deque


def bfs():
    visited[1] = 1
    while queue:
        cur_pos = queue.popleft()
        if cur_pos == 100:
            return
        for plus in range(1, 6 + 1):
            next_pos = cur_pos + plus
            if next_pos > 100:
                continue
            if next_pos in jump:
                next_pos = jump[next_pos]
            if visited[next_pos] == 0:
                visited[next_pos] = visited[cur_pos] + 1
                queue.append(next_pos)


n, m = map(int, input().split())
jump = {}
for _ in range(n + m):
    jump_from, jump_to = map(int, input().split())
    jump[jump_from] = jump_to
visited = [0] * (100 + 1)
queue = deque([1])
bfs()

print(visited[-1] - 1)
