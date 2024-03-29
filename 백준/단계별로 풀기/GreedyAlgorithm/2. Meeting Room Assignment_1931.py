import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: (x[1], x[0]))
count = 0
end_cur = 0
for start, end in arr:
    if start >= end_cur:
        count += 1
        end_cur = end

print(count)
