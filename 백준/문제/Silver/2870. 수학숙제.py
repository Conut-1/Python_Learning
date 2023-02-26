import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    number = ''
    paper = input().strip()
    for chr in paper:
        if chr.isdigit():
            number += chr
        elif number:
            numbers.append(int(number))
            number = ''
    if number:
        numbers.append(int(number))

numbers.sort()
for number in numbers:
    print(number)
