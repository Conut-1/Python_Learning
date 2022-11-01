import sys
input = sys.stdin.readline

def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[- 1 - i]:
            return False
    return True

while True:
    string = input().rstrip()
    if string == '0':
        break
    if is_palindrome(string):
        print('yes')
    else:
        print('no')
