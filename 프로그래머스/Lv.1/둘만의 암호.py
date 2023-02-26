def solution(s, skip, index):
    alpha = []
    for i in range(26):
        if chr(ord('a') + i) not in skip:
            alpha.append(chr(ord('a') + i))
    answer = ''
    for cha in s:
        answer += alpha[(alpha.index(cha) + index) % len(alpha)]
    return answer
