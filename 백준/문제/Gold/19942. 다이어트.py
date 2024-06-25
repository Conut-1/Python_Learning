from itertools import combinations

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

answer_c = 10_000
answer = None
for cnt in range(1, N + 1):
    for comb in combinations(range(N), cnt):
        tp = tf = ts = tv = tc = 0
        for target in comb:
            tp += ingredients[target][0]
            tf += ingredients[target][1]
            ts += ingredients[target][2]
            tv += ingredients[target][3]
            tc += ingredients[target][4]

        if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
            if answer == None or answer_c > tc:
                answer_c = tc
                answer = comb
            elif answer_c == tc:
                answer = sorted((answer, comb))[0]
if answer_c == 10_000 or answer == None:
    print(-1)
else:
    print(answer_c)
    print(*map(lambda x: x + 1, answer))
