import sys
input = sys.stdin.readline

test_case = int(input().strip())
for _ in range(test_case):
    a, b = map(int, input().strip().split())
    print(a+b)