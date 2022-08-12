import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(result)
