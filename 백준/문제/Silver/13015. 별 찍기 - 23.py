def end(n):
    string = '*' * n + ' ' * (2 * n - 3) + '*' * n
    print(string)

def mid(n):
    line = '*' + ' ' * (n - 2) + '*'
    for i in range(n - 2):
        string = ' ' * (i + 1) + line + ' ' * (2 * (n - 2) - 1 - 2 * i) + line
        print(string)
    string = ' ' * (n - 1) + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*'
    print(string)
    for i in range(n - 3, -1, -1):
        string = ' ' * (i + 1) + line + ' ' * (2 * (n - 2) - 1 - 2 * i) + line
        print(string)

N = int(input())

end(N)
mid(N)
end(N)
