def solve():
    arr = list(map(int, input().split()))
    ascend_count = 0
    descend_count = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            ascend_count += 1
        else:
            descend_count += 1
    if ascend_count == 7:
        return "ascending"
    if descend_count == 7:
        return "descending"
    return "mixed"

print(solve())
