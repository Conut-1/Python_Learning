a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(mul)):
    if mul[i] == "0":
        arr[0] += 1
    elif mul[i] == "1":
        arr[1] += 1
    elif mul[i] == "2":
        arr[2] += 1
    elif mul[i] == "3":
        arr[3] += 1
    elif mul[i] == "4":
        arr[4] += 1
    elif mul[i] == "5":
        arr[5] += 1
    elif mul[i] == "6":
        arr[6] += 1
    elif mul[i] == "7":
        arr[7] += 1
    elif mul[i] == "8":
        arr[8] += 1
    elif mul[i] == "9":
        arr[9] += 1
for num in arr:
    print(num)