def solution(s):
    x = None
    x_count = 0
    else_count = 0
    answer = 0
    for cha in s:
        if x_count == else_count:
            answer += 1
            x = cha
        if x == cha:
            x_count += 1
        else:
            else_count += 1
    return answer
