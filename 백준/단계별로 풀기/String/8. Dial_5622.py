input_value = input()
number = []
result = 0
for i in input_value:
    if i in "ABC":
        number.append(2)
    elif i in "DEF":
        number.append(3)
    elif i in "GHI":
        number.append(4)
    elif i in "JKL":
        number.append(5)
    elif i in "MNO":
        number.append(6)
    elif i in "PQRS":
        number.append(7)
    elif i in "TUV":
        number.append(8)
    elif i in "WXYZ":
        number.append(9)
for i in number:
    result += i + 1
print(result)