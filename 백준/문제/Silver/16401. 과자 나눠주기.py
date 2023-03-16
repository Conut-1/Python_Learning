def search():
    start = 1
    end = 1_000_000_000

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for s in snacks:
            count += s // mid

        if count >= M:
            start = mid + 1
        else:
            end = mid - 1

    return end


M, N = map(int, input().split())
snacks = list(map(int, input().split()))

print(search())
