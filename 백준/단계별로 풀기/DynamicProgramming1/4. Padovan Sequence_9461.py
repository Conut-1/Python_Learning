import sys
input = sys.stdin.readline

def wave(n):
    if not n in dict:
        dict[n] = wave(n - 1) + wave(n - 5)
    return dict[n]

t = int(input())
dict = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9}
for _ in range(t):
    len = int(input())

    print(wave(len))
