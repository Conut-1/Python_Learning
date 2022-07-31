def recursive(num):
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        return num * recursive(num - 1)

input = int(input())
print(recursive(input))