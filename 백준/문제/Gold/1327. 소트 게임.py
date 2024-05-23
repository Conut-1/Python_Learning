from collections import deque

N, K = map(int, input().split())
seq = list(map(int, input().split()))

visited = set(["".join(map(str, seq))])
target = [i for i in range(1, N + 1)]
answer = -1
queue = deque([(seq, 0)])

while queue:
    cur, count = queue.popleft()
    if cur == target:
        answer = count
        break
    for i in range(N - K + 1):
        new_seq = cur[:i] + list(reversed(cur[i : i + K])) + cur[i + K :]
        new_str = "".join(map(str, new_seq))
        if new_str not in visited:
            queue.append((new_seq, count + 1))
            visited.add(new_str)

print(answer)
