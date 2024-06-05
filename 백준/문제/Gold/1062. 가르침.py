def solve():
    N, K = map(int, input().split())
    words = [input() for _ in range(N)]

    if K < 5:
        return 0

    if K == 26:
        return N

    converts = []
    for word in words:
        num = 0
        for c in set(word):
            num |= 1 << (ord(c) - ord("a"))
        converts.append(num)

    learn = 0
    for c in ["a", "n", "t", "i", "c"]:
        learn |= 1 << (ord(c) - ord("a"))

    res = 0

    def dfs(learn, idx, count):
        nonlocal res

        if count == K:
            count = 0
            for c in converts:
                if c & learn == c:
                    count += 1
            res = max(res, count)
            return

        for i in range(idx, 26):
            if learn & (1 << i):
                continue
            dfs(learn | (1 << i), i, count + 1)

    dfs(learn, 0, 5)

    return res


print(solve())
