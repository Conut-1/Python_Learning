from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
grid = [[deque() for _ in range(N)] for _ in range(N)]

mass = 0
for _ in range(M):
    r, c, m, s, d = tuple(map(int, input().split()))
    mass += m
    grid[r - 1][c - 1].append((m, s, d, 0))

for counter in range(K):
    for i in range(N):
        for j in range(N):
            while grid[i][j] and grid[i][j][0][-1] == counter:
                m, s, d, count = grid[i][j].popleft()
                next_r = (N + i + dr[d] * (s % N)) % N
                next_c = (N + j + dc[d] * (s % N)) % N
                grid[next_r][next_c].append((m, s, d, count + 1))

    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) < 2:
                continue
            m_sum = 0
            s_sum = 0
            d_check = True
            first_d = grid[i][j][0][2]
            ball_count = 0
            while grid[i][j]:
                m, s, d, _ = grid[i][j].popleft()
                mass -= m
                m_sum += m
                s_sum += s
                ball_count += 1
                if d_check:
                    d_check = (first_d % 2 == 0) == (d % 2 == 0)

            if m_sum // 5 == 0:
                continue

            mass += 4 * (m_sum // 5)
            for k in range(4):
                direction_add = 0 if d_check else 1
                grid[i][j].append(
                    (
                        m_sum // 5,
                        s_sum // ball_count,
                        2 * k + direction_add,
                        counter + 1,
                    )
                )

print(mass)
