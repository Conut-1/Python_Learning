test = int(input())

for i in range(test):
    count = 0
    result = 0
    arr = input()
    for j in range(len(arr)):
        if arr[j] == "O":
            count += 1
            result += count
        else:
            count = 0

    print(result)