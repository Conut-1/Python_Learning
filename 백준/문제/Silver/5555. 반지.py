import sys
input = sys.stdin.readline

string = input().rstrip()
N = int(input())
count = 0
for _ in range(N):
    ring_str = input().rstrip()
    ring_str += ring_str
    if string in ring_str:
        count += 1

print(count)
