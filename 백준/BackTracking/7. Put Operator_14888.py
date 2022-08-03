def dfs(output, i):
    if i == n - 1:
        if len(res) == 0:
            res.append(output)
            res.append(output)
        else:
            if res[0] > output:
                res[0] = output
            if res[1] < output:
                res[1] = output
        return
    for j in range(4):
        if operator[j] != 0:
            operator[j] -= 1
            if j == 0:
                dfs(output + a[i + 1], i + 1)
            elif j == 1:
                dfs(output - a[i + 1], i + 1)
            elif j == 2:
                dfs(output * a[i + 1], i + 1)
            else:
                dfs(int(output / a[i + 1]), i + 1)
            operator[j] += 1

n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))
res = []

dfs(a[0], 0)
print(res[1])
print(res[0])
