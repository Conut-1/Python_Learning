from itertools import combinations
import sys

input = sys.stdin.readlines

scores = [list(map(int, score.split())) for score in input()]


def dfs(count, win, draw, loss):
    if count == 15:
        global ans
        if win.count(0) == 6 and draw.count(0) == 6 and loss.count(0) == 6:
            ans = 1
        return

    home, away = match[count]
    if win[home] > 0 and loss[away] > 0:
        win[home] -= 1
        loss[away] -= 1
        dfs(count + 1, win, draw, loss)
        win[home] += 1
        loss[away] += 1
    if draw[home] > 0 and draw[away] > 0:
        draw[home] -= 1
        draw[away] -= 1
        dfs(count + 1, win, draw, loss)
        draw[home] += 1
        draw[away] += 1
    if loss[home] > 0 and win[away] > 0:
        loss[home] -= 1
        win[away] -= 1
        dfs(count + 1, win, draw, loss)
        loss[home] += 1
        win[away] += 1


res = [0] * len(scores)
match = list(combinations(range(6), 2))
for i, score in enumerate(scores):
    win = score[::3]
    draw = score[1::3]
    loss = score[2::3]
    ans = 0
    dfs(0, win, draw, loss)
    res[i] = ans


print(*res)
