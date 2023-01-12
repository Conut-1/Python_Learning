def cal_min():
    for i in range(6):
        if minimum[0] > dice[i]:
            minimum[0] = dice[i]
        for j in range(i + 1, 6):
            if i + j == 5:
                continue
            if minimum[1] > dice[i] + dice[j]:
                minimum[1] = dice[i] + dice[j]
            for k in range(j + 1, 6):
                if i + k == 5 or j + k == 5:
                    continue
                if minimum[2] > dice[i] + dice[j] + dice[k]:
                    minimum[2] = dice[i] + dice[j] + dice[k]

def solve():
    if N == 1:
        return sum(dice) - max(dice)
    else:
        res = 0
        res += minimum[0] * ((N - 2) ** 2 + 4 * (N - 1) * (N - 2))
        res += minimum[1] * (4 * (N - 1) + 4 * (N - 2))
        res += minimum[2] * 4
        return res


N = int(input())
dice = list(map(int, input().split()))

minimum = [sum(dice)] * 3
cal_min()
print(solve())

# n = int(input())
# a = list(map(int, input().split()))
# min = [min(a[0], a[5]), min(a[1], a[4]), min(a[2], a[3])]
# min.sort()
# if n >= 2:
#     print(min[2]*4+min[1]*8*(n-1)+min[0]*(5*(n**2)-8*n+4))
# else:
#     print(sum(a)-max(a))
