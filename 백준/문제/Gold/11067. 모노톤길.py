import sys
input = sys.stdin.readline


def cafe_sort(cafe):
    cafe.sort(key=lambda x: (x[0], x[1]))

    same_y = [(-1, 0)]
    cur_x = -1
    for i in range(n):
        if cur_x == cafe[i][0]:
            same_y.append(cafe[i])
        else:
            if cafe_seq[-1][1] != same_y[0][1]:
                same_y.reverse()
            cafe_seq.extend(same_y)
            same_y = [cafe[i]]
            cur_x = cafe[i][0]
    
    if same_y[0] not in cafe_seq:
        if cafe[-1][1] != same_y[0][1]:
            same_y.sort(reverse=True)
        cafe_seq.extend(same_y)


T = int(input())
for _ in range(T):
    n = int(input())
    cafe = [tuple(map(int, input().split())) for _ in range(n)]
    cafe_seq = [(-1, 0)]

    cafe_sort(cafe)

    m, *targets = map(int, input().split())
    for target in targets:
        print(*cafe_seq[target + 1])
