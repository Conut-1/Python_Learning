def next_permutation(arr):
    for i in range(N - 1, 0, -1):
        if arr[i - 1] < arr[i]:
            for j in range(N - 1, 0, -1):
                if arr[i - 1] < arr[j]:
                    arr[i - 1], arr[j] = arr[j], arr[i - 1]
                    arr = arr[:i] + sorted(arr[i:])
                    return arr
    return [-1]


N = int(input())
arr = list(map(int, input().split()))

print(*next_permutation(arr))
