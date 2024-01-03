n = int(input())
cases = [input() for _ in range(n)]

for case in cases:
    size = int(len(case) ** 0.5)
    arr = [case[i * size : (i + 1) * size] for i in range(size)]
    res = ""
    for i in range(len(case)):
        res += arr[i % size][size - i // size - 1]
    print(res)
