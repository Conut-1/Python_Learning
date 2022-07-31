x_set = set()
y_set = set()

for _ in range(3):
    pos_x, pos_y = list(map(int, input().split()))

    if pos_x in x_set:
        x_set.remove(pos_x)
    else:
        x_set.add(pos_x)
    if pos_y in y_set:
        y_set.remove(pos_y)
    else:
        y_set.add(pos_y)

pos_4_x = list(x_set)[0]
pos_4_y = list(y_set)[0]

print(pos_4_x, pos_4_y)