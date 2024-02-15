import sys

input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    k, *t_arr = map(int, input().split())
    info = 0
    for t in t_arr:
        info |= 1 << (t - 1)
    classes.append(info)

m = int(input())
students = []
for _ in range(m):
    p, *q_arr = map(int, input().split())
    info = 0
    for q in q_arr:
        info |= 1 << (q - 1)
    students.append(info)

for student in students:
    count = 0
    for c in classes:
        if c == student & c:
            count += 1
    print(count)
