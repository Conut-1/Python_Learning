from itertools import permutations
import sys
input = sys.stdin.readline

def count_strike(q, target):
    count = 0
    for i in range(3):
        if q[i] == target[i]:
            count += 1
    return count

def count_ball(q, target):
    count = 0
    for i in range(3):
        if q[i] in target:
            count += 1
    return count

digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
possible = set(map(''.join, permutations(digit, 3)))

N = int(input())
for _ in range(N):
    q, strike, ball = input().split()
    new_possible = set()
    for target in possible:
        if count_strike(q, target) == int(strike) and count_ball(q, target) == int(ball) + int(strike):
            new_possible.add(target)
    possible = new_possible

print(len(possible))
