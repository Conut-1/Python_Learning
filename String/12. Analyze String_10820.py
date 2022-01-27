while True:
    try:
        input_value = input()
        arr = [0] * 4
        for i in input_value:
            if i.islower():
                arr[0] += 1
            elif i.isupper():
                arr[1] += 1
            elif i.isdecimal():
                arr[2] += 1
            else:
                arr[3] += 1
        print(*arr)
    except:
        break