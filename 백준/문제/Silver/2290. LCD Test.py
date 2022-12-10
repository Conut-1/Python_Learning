top = [0, 2, 3, 5, 6, 7, 8, 9]
left_up = [0, 4, 5, 6, 8, 9]
right_up = [0, 1, 2, 3, 4, 7, 8, 9]
middle = [2, 3, 4, 5, 6, 8, 9]
left_down = [0, 2, 6, 8]
rigth_down = [0, 1, 3, 4, 5, 6, 7, 8, 9]
bottom = [0, 2, 3, 5, 6, 8, 9]

def set_num(num, x):
    if num in top:
        for i in range(s):
            display[0][x + i + 1] = '-'
    if num in left_up:
        for i in range(s):
            display[i + 1][x] = '|'
    if num in right_up:
        for i in range(s):
            display[i + 1][x + s + 1] = '|'
    if num in middle:
        for i in range(s):
            display[s + 1][x + i + 1] = '-'
    if num in left_down:
        for i in range(s):
            display[i + s + 2][x] = '|'
    if num in rigth_down:
        for i in range(s):
            display[i + s + 2][x + s + 1] = '|'
    if num in bottom:
        for i in range(s):
            display[2 * s + 2][x + i + 1] = '-'

s, n = input().split()
s = int(s)

display = [[' '] * ((s + 2 + 1) * len(n) - 1) for _ in range(2 * s + 3)]

for i in range(len(n)):
    set_num(int(n[i]), i * (s + 3))

for line in display:
    print(('').join(line))
