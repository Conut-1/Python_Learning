def solution(maps):
    from collections import deque

    def escape(x, y):
        visited_1[x][y] = 1
        queue = deque([(x, y, 0)])
        while queue:
            cur_x, cur_y, cur_time = queue.popleft()
            if maps[cur_x][cur_y] == "L":
                visited_2[cur_x][cur_y] = 1
                queue = deque([(cur_x, cur_y, cur_time)])
                break
            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if not (0 <= next_x < height and 0 <= next_y < width):
                    continue
                if maps[next_x][next_y] == "X":
                    continue
                if visited_1[next_x][next_y] == 1:
                    continue
                visited_1[next_x][next_y] = 1
                queue.append((next_x, next_y, cur_time + 1))

        while queue:
            cur_x, cur_y, cur_time = queue.popleft()
            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if not (0 <= next_x < height and 0 <= next_y < width):
                    continue
                if maps[next_x][next_y] == "X":
                    continue
                if visited_2[next_x][next_y] == 1:
                    continue
                if maps[next_x][next_y] == "E":
                    return cur_time + 1
                visited_2[next_x][next_y] = 1
                queue.append((next_x, next_y, cur_time + 1))
        return -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    height = len(maps)
    width = len(maps[0])
    visited_1 = [[0] * width for _ in range(height)]
    visited_2 = [[0] * width for _ in range(height)]

    answer = -1
    for i in range(height):
        for j in range(width):
            if maps[i][j] == "S":
                return escape(i, j)
    return answer
