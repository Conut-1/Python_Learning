import sys
input = sys.stdin.readline

def solve():
    for i in range(N):
        for j in range(i, N):
            if words[i][j] != words[j][i]:
                return "NO"
    return "YES"

N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

print(solve())
