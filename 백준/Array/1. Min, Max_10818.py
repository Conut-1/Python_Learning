number = input()
integer = list(map(int, input().split()))
max = integer[0]
min = integer[0]
for i in integer:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)