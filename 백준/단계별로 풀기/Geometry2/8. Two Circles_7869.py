import math

x_1, y_1, r_1, x_2, y_2, r_2 = map(float, input().split())

d = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
if d > r_1 + r_2:
    res = 0
elif (d <= abs(r_1 - r_2) and r_1 < r_2):
    res = math.pi * r_1 * r_1
elif (d <= abs(r_1 - r_2) and r_1 >= r_2):
    res = math.pi * r_2 * r_2
else:
    theta_1 = 2 * math.acos((r_1 ** 2 + d ** 2 - r_2 ** 2) / (2 * r_1 * d))
    theta_2 = 2 * math.acos((r_2 ** 2 + d ** 2 - r_1 ** 2) / (2 * r_2 * d))

    area_1 = r_1 * r_1 * theta_1 / 2 - r_1 * r_1 * math.sin(theta_1) / 2
    area_2 = r_2 * r_2 * theta_2 / 2 - r_2 * r_2 * math.sin(theta_2) / 2

    res = area_1 + area_2

print(f'{res:.3f}')
