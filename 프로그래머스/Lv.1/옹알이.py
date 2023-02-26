def solve(b):
    possible = ["aya", "ye", "woo", "ma"]
    i = 0
    prev = ''
    while i < len(b):
        for p in possible:
            if p == b[i:i + len(p)] and prev != p:
                i += len(p)
                prev = p
                break
        else:
            return False
    return True

def solution(babbling):
    answer = 0
    for b in babbling:
        if solve(b):
            answer += 1
    return answer
