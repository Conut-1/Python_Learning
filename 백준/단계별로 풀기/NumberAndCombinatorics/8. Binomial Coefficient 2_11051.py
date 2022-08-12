import sys
sys.setrecursionlimit(1002)

def factorial(dict, n):
    if not n in dict:
        dict[n] = n * factorial(dict, n - 1)
    return dict[n]

n, k = map(int, input().split())

dict = {0: 1, 1: 1}
result = factorial(dict, n) // (factorial(dict, k) * factorial(dict, n - k))
print(result % 10007)
