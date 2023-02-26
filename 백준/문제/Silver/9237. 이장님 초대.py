N = int(input())
t = list(map(int, input().split()))

finish = 0
t.sort(reverse=True)
for i in range(len(t)):
    if finish < (i + 1) + t[i] + 1:
        finish = (i + 1) + t[i] + 1

print(finish)
