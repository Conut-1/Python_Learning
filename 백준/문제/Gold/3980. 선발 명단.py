import sys

input = sys.stdin.readline

c = int(input())


def calculate(stats):
    max_value = 0
    used = [0] * 11

    def bf(count, sum):
        nonlocal max_value
        if count == 11:
            max_value = sum if sum > max_value else max_value
            return

        for i in range(11):
            if not used[i] and stats[count][i]:
                used[i] = 1
                sum += stats[count][i]
                bf(count + 1, sum)
                sum -= stats[count][i]
                used[i] = 0

    bf(0, 0)
    return max_value


for _ in range(c):
    stats = [list(map(int, input().split())) for _ in range(11)]
    print(calculate(stats))
