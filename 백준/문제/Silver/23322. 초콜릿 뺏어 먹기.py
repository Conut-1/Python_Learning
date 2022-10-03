N, K = map(int, input().split())
chocolates = list(map(int, input().split()))

if K >= N:
    print("0 0")
else:
    count = 0
    day = 0
    for chocolate in chocolates[1:]:
        if chocolate != chocolates[0]:
            count += chocolate - chocolates[0]
            day += 1
    print(count, day)
