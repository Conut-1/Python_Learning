def gcf(x, y):
    if x % y == 0:
        return y
    else:
        return gcf(y, x % y)

n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    factor = gcf(arr[0], arr[i + 1])
    numerator = arr[0] // factor
    denominator = arr[i + 1] // factor
    print(f"{numerator}/{denominator}")
