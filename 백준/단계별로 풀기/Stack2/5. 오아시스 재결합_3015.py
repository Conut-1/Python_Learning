import sys
input = sys.stdin.readline

N = int(input())
people = [int(input()) for _ in range(N)]

stack = []
count = 0

for person in people:
    while stack and stack[-1][0] < person:
        count += stack.pop()[1]
    if not stack:
        stack.append([person, 1])
        continue
    if person == stack[-1][0]:
        count += stack[-1][1]
        if len(stack) > 1:
            count += 1
        stack[-1][1] += 1
    else:
        count += 1
        stack.append([person, 1])

print(count)
