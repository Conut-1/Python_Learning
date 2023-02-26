def solve():
    count = 0
    while arr:
        if arr[-1] == '(':
            arr.pop()
            return count * int(arr.pop())
        if arr[-1] == ')':
            arr.pop()
            count += solve()
        else:
            arr.pop()
            count += 1
    return count


S = input()

arr = list(str(S))
print(solve())
