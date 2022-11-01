import sys
input = sys.stdin.readline

N, M = map(int, input().split())

passwords = {}
for _ in range(N):
    address, password = input().split()
    passwords[address] = password

for _ in range(M):
    address = input().rstrip()
    print(passwords[address])
