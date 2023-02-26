def solution(X, Y):
    answer = ''
    digit = [0] * 10
    for i in range(10):
        digit[i] = min(X.count(str(i)), Y.count(str(i)))
    for i in range(9, 0, -1):
        answer += str(i) * digit[i]
    if not answer and digit[0] > 0:
        answer = '0'
    else:
        answer += str(0) * digit[0]
    if not answer:
        answer = '-1'
    return answer
