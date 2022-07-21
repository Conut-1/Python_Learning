def fibonacci(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)

input = int(input())
print(fibonacci(input))