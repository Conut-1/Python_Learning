import sys
sys.stdin.readline

def digit_sum(a):
    count = 0
    for cha in a:
        if ord('1') <= ord(cha) <= ord('9'):
            count += int(cha)
    return count

N = int(input())
serials = [input().rstrip() for _ in range(N)]
serials.sort(key=lambda x: (len(x), digit_sum(x), x))

print(*serials, sep='\n')
