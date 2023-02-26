import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(float(input()))

scores.sort()
for i in range(7):
    print(f'{scores[i]:.3f}')
