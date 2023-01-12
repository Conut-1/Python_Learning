K = int(input())

digit = [4, 7]
res = ''
num = K + 1
while num:
    res = str(digit[num % 2]) + res
    num //= 2

print(res[1:])
