def make_it_1(n):
    for i in range(2, n + 1):
        dict[i] = dict[i - 1] + 1
        if i % 3 == 0:
            dict[i] = min(dict[i], dict[i // 3] + 1)
        if i % 2 == 0:
            dict[i] = min(dict[i], dict[i // 2] + 1)
    return dict[n]

n = int(input())

dict = {1: 0}

print(make_it_1(n))
