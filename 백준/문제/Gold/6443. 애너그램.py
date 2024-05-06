import sys

input = sys.stdin.readline


def back_tracking(cnt):
    if cnt == len(word):
        print("".join(answer))
        return

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            answer.append(k)
            back_tracking(cnt + 1)
            visited[k] += 1
            answer.pop()


n = int(input())

for _ in range(n):
    word = sorted(list(input().strip()))
    visited = {}
    answer = []

    for i in word:
        if i not in visited:
            visited[i] = 0
        visited[i] += 1

    back_tracking(0)
