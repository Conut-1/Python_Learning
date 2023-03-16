def solution(cards):
    def cycle(start):
        visited[start] = 1
        cur = start
        count = 1
        while visited[cards[cur - 1]] == 0:
            cur = cards[cur - 1]
            visited[cur] = 1
            count += 1
        return count

    cycles = []
    visited = [0] * (len(cards) + 1)
    for i in range(1, len(cards) + 1):
        if visited[i] == 1:
            continue
        cycles.append(cycle(i))

    cycles.sort()
    answer = cycles[-1] * cycles[-2] if len(cycles) > 1 else 0

    return answer
