A, B, C = map(int, input().split())

if B > C:
    print(A * B // C)
else:
    print(A * C // B)
