def draw(n):
    if n == 1:
        return ["*"]

    stars = draw(n // 3)

    lst = []
    for str in stars:
        lst.append(str * 3)
    for str in stars:
        lst.append(str + ' ' * (n // 3)+ str)
    for str in stars:
        lst.append(str * 3)
    return lst
input = int(input())
print("\n".join(draw(input)))

# def set_arr(arr, col, row, input, space):
#     if input == 1:
#         if space == 1:
#             arr[col][row] = ' '
#         elif col // 3 == 1 and row // 3 == 1:
#             arr[col][row] = ' '
#         else:
#             arr[col][row] = '*'
#     else:
#         for i in range(3):
#             for j in range(3):
#                 if (i == 1 and j == 1) or space == 1:
#                     set_arr(arr, (input // 3) * i + col, (input // 3) * j + row, input // 3, 1)
#                 else:
#                     set_arr(arr, (input // 3) * i + col, (input // 3) * j + row, input // 3, 0)

# input = int(input())
# arr = [[0 for col in range(input)] for row in range(input)]
# set_arr(arr, 0, 0, input, 0)
# for i in range(input):
#     print(''.join(arr[i]))