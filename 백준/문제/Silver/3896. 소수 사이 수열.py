import sys

input = sys.stdin.readline

MAX_P = 1299709
num_arr = [True] * (MAX_P + 1)
m = int(MAX_P**0.5)
for i in range(2, m + 1):
    if num_arr[i] == True:
        for j in range(i * i, MAX_P + 1, i):
            num_arr[j] = False
prime_arr = [i for i in range(2, MAX_P + 1) if num_arr[i] == True]

t = int(input())
for _ in range(t):
    k = int(input())
    res = 0
    for i in range(len(prime_arr)):
        if k == prime_arr[i]:
            break
        if prime_arr[i] > k:
            res = prime_arr[i] - prime_arr[i - 1]
            break
    print(res)
