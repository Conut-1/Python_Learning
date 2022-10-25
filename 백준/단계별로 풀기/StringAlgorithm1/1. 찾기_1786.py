def get_pi(p, pi):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(t, p, res):
    pi = [0] * len(p)
    get_pi(P, pi)
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pi[j - 1]
        if t[i] == p[j]:
            if j == len(p) - 1:
                res.append(i - len(p) + 2)
                j = pi[j]
            else:
                j += 1

T = input()
P = input()

res = []
kmp(T, P, res)
print(len(res))
print(*res)
