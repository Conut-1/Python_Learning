import sys
input = sys.stdin.readline

def get_column(m):
    column = ''
    while m:
        m -= 1
        index = m % 26
        column = chr(ord("A") + index) + column
        m //= 26
    return column

while True:
    n, m = map(int, input()[1:].split('C'))
    if n == 0 and m == 0:
        break
    print(f'{get_column(m)}{n}')
