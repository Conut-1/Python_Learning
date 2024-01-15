n = int(input())
cur = n // 2
start = 1
end = n

while start < end:
    mid = (start + end) // 2
    if mid**2 >= n:
        end = mid
    else:
        start = mid + 1

print(end)
