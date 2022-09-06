from itertools import combinations


def solution():
    global N
    global C

    if N == 1 and items[0] <= C:
        return 2
    if N == 1 and items[0] > C:
        return 1

    item_left, item_right = items[:N // 2], items[N // 2:]
    sub_left, sub_right = [0], [0]

    for i in range(1, len(item_left) + 1):
        for sub in combinations(item_left, i):
            sub_left.append(sum(sub))
    sub_left.sort()

    for i in range(1, len(item_right) + 1):
        for sub in combinations(item_right, i):
            sub_right.append(sum(sub))
    sub_right.sort()

    answer = 0
    for i in sub_right:
        if i > C:
            continue
        left = 0
        right = len(sub_left)
        while left < right:
            mid = (left + right) // 2
            if sub_left[mid] + i > C:
                right = mid
            else:
                left = mid + 1
        answer += right

    return answer


N, C = map(int, input().split())
items = list(map(int, input().split()))

print(solution())
