def count_five(n):
    cnt = 0
    while n >= 5:
        n //= 5
        cnt +=n
    return cnt

def count_two(n):
    cnt = 0
    while n >= 2:
        n //= 2
        cnt +=n
    return cnt
    
n, m = map(int, input().split())

print(min(count_five(n) - count_five(m) - count_five(n - m), count_two(n) - count_two(m) - count_two(n - m)))
