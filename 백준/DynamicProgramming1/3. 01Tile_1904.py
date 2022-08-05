def tile(n):
    dict = {1: 1, 2: 2}
    for i in range(3, n + 1):
        dict[i] = (dict[i - 1] + dict[i - 2]) % 15746
    return dict[n]

n = int(input())
print(tile(n))
