A = input()
B = input()

array = [0] * (2 * len(A))
for i in range(len(A)):
    array[i * 2] = int(A[i])
    array[i * 2 + 1] = int(B[i])

while len(array) != 2:
    for i in range(len(array) - 1):
        array[i] = (array[i] + array[i + 1]) % 10
    array.pop()

print(''.join(map(str, array)))
