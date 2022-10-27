import math

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    floor = str(N % H if N % H != 0 else H)
    room_num = str(math.ceil(N / H)).zfill(2)

    print(floor + room_num)
