def fib(n):
    global count_recur
    if n == 1 or n == 2:
        count_recur += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global count_dp
    f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        count_dp += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
res = []
f = {}
count_recur = 0
count_dp = 0
fib(n)
fibonacci(n)
print(count_recur, count_dp)
