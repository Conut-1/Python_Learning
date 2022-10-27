import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

def recursion(string, l, r):
    global count

    count += 1
    if l >= r:
        return 1
    elif string[l] != string[r]:
        return 0
    else:
        return recursion(string, l + 1, r - 1)

def is_palindrome(string):
    return recursion(string, 0, len(string) - 1)

T = int(input())
for _ in range(T):
    count = 0
    string = input().rstrip()
    print(is_palindrome(string), count)
