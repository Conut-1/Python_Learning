def hanoi(arr, num, start, target):
    if num == 1:
        arr.append(str(start) + " " + str(target))
    else:
        hanoi(arr, num - 1, start, 6 - start - target)
        arr.append(str(start) + " " + str(target))
        hanoi(arr, num - 1, 6 - start - target, target)

arr = []
input = int(input())
hanoi(arr, input, 1, 3)
print(len(arr))
print("\n".join(arr))