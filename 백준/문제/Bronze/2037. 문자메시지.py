p, w = map(int, input().split())
string = input()

key = {}
key[1] = ' '
key[2] = 'ABC'
key[3] = 'DEF'
key[4] = 'GHI'
key[5] = 'JKL'
key[6] = 'MNO'
key[7] = 'PQRS'
key[8] = 'TUV'
key[9] = 'WXYZ'

prev = 0
time = 0
for chr in string:
    for i in range(1, 1 + 9):
        if chr in key[i]:
            time += p * (key[i].find(chr) + 1)
            if i != 1 and i == prev:
                time += w
            prev = i
            break

print(time)
