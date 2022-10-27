def merge_sort(arr, tmp, l, r, k):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, tmp, l, mid, k)
        merge_sort(arr, tmp, mid + 1, r, k)
        merge(arr, tmp, l, mid, r, k)

def merge(arr, tmp, l, mid, r, k):
    global count
    global res

    i = l
    j = mid + 1
    t = 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while i <= mid:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = l
    t = 0
    while i <= r:
        count += 1
        if count == k:
            res = tmp[t]
        arr[i] = tmp[t]
        i += 1
        t += 1

N, K = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [0] * len(arr)

count = 0
res = -1
merge_sort(arr, tmp, 0, len(arr) - 1, K)
print(res)
