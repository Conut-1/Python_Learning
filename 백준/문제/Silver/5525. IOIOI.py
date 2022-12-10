def get_pi(p, pi):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j

def kmp(s, p):
    count = 0

    pi = [0] * len(p)
    get_pi(p, pi)

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                count += 1
                j = pi[j]
            else:
                j += 1
    
    return count

N = int(input())
P = "IO" * N + "I"

M = int(input())
S = input()

print(kmp(S, P))
