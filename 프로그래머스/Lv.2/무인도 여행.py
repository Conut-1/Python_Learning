def dfs(x, y, maps, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    width = len(maps[0])
    height = len(maps)
    count = 0

    stack = [(x, y)]
    visited[x][y] = 1
    count += int(maps[x][y])
    
    while stack:
        cur_x, cur_y = stack.pop()
        for x_diff, y_diff in zip(dx, dy):
            next_x, next_y = cur_x + x_diff, cur_y + y_diff
            if not (0 <= next_x < height and 0 <= next_y < width):
                continue
            if visited[next_x][next_y] or maps[next_x][next_y] == 'X':
                continue
            stack.append((next_x, next_y))
            visited[next_x][next_y] = 1
            count += int(maps[next_x][next_y])

    return count

def solution(maps):
    width = len(maps[0])
    height = len(maps)
    visited = [[0] * width for _ in range(height)]

    answer = []
    for i in range(height):
        for j in range(width):
            if not (visited[i][j] or maps[i][j] == 'X'):
                answer.append(dfs(i, j, maps, visited))

    answer.sort()
    if not answer:
        answer.append(-1)
    return answer
