def ccw(pos_1, pos_2, pos_3):
    a = pos_1[0] * pos_2[1] + pos_2[0] * pos_3[1] + pos_3[0] * pos_1[1]
    b = pos_1[1] * pos_2[0] + pos_2[1] * pos_3[0] + pos_3[1] * pos_1[0]
    return a - b

def solve(pos_1, pos_2, pos_3, pos_4):
    a = ccw(pos_1, pos_2, pos_3)
    b = ccw(pos_1, pos_2, pos_4)
    c = ccw(pos_3, pos_4, pos_1)
    d = ccw(pos_3, pos_4, pos_2)
    if a * b == 0 and c * d == 0:
        if pos_1 > pos_2:
            pos_1, pos_2 = pos_2, pos_1
        if pos_3 > pos_4:
            pos_3, pos_4 = pos_4, pos_3
        if pos_3 <= pos_2 and pos_1 <= pos_4:
            return 1
        return 0
    if a * b <= 0 and c * d <= 0:
        return 1
    return 0

x_1, y_1, x_2, y_2 = map(int, input().split())
x_3, y_3, x_4, y_4 = map(int, input().split())

pos_1 = (x_1, y_1)
pos_2 = (x_2, y_2)
pos_3 = (x_3, y_3)
pos_4 = (x_4, y_4)

if solve(pos_1, pos_2, pos_3, pos_4) == 1:
    try:
        print(1)
        p_x = ((x_1 * y_2 - y_1 * x_2) * (x_3 - x_4) - (x_1 - x_2) * (x_3 * y_4 - y_3 * x_4)) / ((x_1 - x_2) * (y_3 - y_4) - (y_1 - y_2) * (x_3 - x_4))
        p_y = ((x_1 * y_2 - y_1 * x_2) * (y_3 - y_4) - (y_1 - y_2) * (x_3 * y_4 - y_3 * x_4)) / ((x_1 - x_2) * (y_3 - y_4) - (y_1 - y_2) * (x_3 - x_4))
        print(p_x, p_y)
    except:
        if pos_1 > pos_2:
            pos_1, pos_2 = pos_2, pos_1
        if pos_3 > pos_4:
            pos_3, pos_4 = pos_4, pos_3
        if pos_2 == pos_3:
            print(pos_2[0], pos_2[1])
        elif pos_1 == pos_4:
            print(pos_1[0], pos_1[1])
else:
    print(0)
