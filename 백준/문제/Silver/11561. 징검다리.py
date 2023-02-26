import sys
input = sys.stdin.readline

def search(n):
    start = 1
    end = int(n ** 0.5 * 2)
    while start <= end:
        mid = (start + end) // 2
        if mid * (mid + 1) <= 2 * n:
            start = mid + 1
        else:
            end = mid - 1
    return end

T = int(input())
for _ in range(T):
    N = int(input())
    print(search(N))
