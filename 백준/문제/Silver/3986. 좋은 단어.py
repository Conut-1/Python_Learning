import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

count = 0
for word in words:
    stack = []
    for chr in word:
        if stack and stack[-1] == chr:
            stack.pop()
        else:
            stack.append(chr)
    if not stack:
        count += 1

print(count)
