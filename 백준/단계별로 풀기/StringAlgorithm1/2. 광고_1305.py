def get_pi(ad, pi):
    j = 0
    for i in range(1, len(ad)):
        while j > 0 and ad[i] != ad[j]:
            j = pi[j - 1]
        if ad[i] == ad[j]:
            j += 1
            pi[i] = j
    return pi

L = int(input())
AD = input()

pi = [0] * L
get_pi(AD, pi)

print(L - pi[-1])
