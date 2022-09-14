def make_it_1(n):
    for i in range(2, n + 1):
        dict[i] = dict[i - 1].copy()
        dict[i].append(i)
        if i % 3 == 0:
            if len(dict[i]) > len(dict[i // 3]) + 1:
                dict[i] = dict[i // 3].copy()
                dict[i].append(i)
        if i % 2 == 0:
            if len(dict[i]) > len(dict[i // 2]) + 1:
                dict[i] = dict[i // 2].copy()
                dict[i].append(i)
    return dict[n]

n = int(input())

dict = {1: [1]}

res = make_it_1(n)
res.reverse()

print(len(res) - 1)
print(*res)
