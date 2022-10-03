import sys
input = sys.stdin.readline

def solution():
    for test, answer in sample_test:
        if test != answer:
            return "Wrong Answer"
    for test, answer in system_test:
        if test != answer:
            return "Why Wrong!!!"
    return "Accepted"


s_1, s_2 = map(int, input().split())
sample_test = [list(map(int, input().split())) for _ in range(s_1)]
system_test = [list(map(int, input().split())) for _ in range(s_2)]

print(solution())
