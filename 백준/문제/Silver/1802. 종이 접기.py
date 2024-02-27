import sys

input = sys.stdin.readline


def is_possible(paper):
    size = len(paper)
    while size != 1:
        mid = size // 2
        for i in range(1, mid + 1):
            if paper[mid - i] == paper[mid + i]:
                return False
        size //= 2
    return True


t = int(input())
for _ in range(t):
    paper = input().rstrip()
    if is_possible(paper):
        print("YES")
    else:
        print("NO")
