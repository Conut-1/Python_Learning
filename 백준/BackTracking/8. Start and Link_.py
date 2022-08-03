import sys
input = sys.stdin.readline

def get_status_diff():
    res = 0

    for i in range(1, n + 1):
        if not i in team_1:
            team_2.append(i)
    for i in range(0, n // 2 - 1):
        for j in range(i + 1, n // 2):
            res += status[team_1[i] - 1][team_1[j] - 1] + status[team_1[j] - 1][team_1[i] - 1]
            res -= status[team_2[i] - 1][team_2[j] - 1] + status[team_2[j] - 1][team_2[i] - 1]
    team_2.clear()
    return abs(res)

def dfs(i):
    if i == n // 2:
        res = get_status_diff()
        if res == 0:
            print(res)
            quit()
        if len(min) == 0:
            min.append(res)
        elif min[0] > res:
            min[0] = res
    else:
        for j in range(1, n + 1):
            if i == 0 or team_1[i - 1] < j:
                team_1.append(j)
                dfs(i + 1)
                team_1.pop()

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]
team_1 = []
team_2 = []
min = []

dfs(0)
print(min[0])
