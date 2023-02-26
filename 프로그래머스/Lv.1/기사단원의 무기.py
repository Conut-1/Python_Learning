def solution(number, limit, power):
    answer = 0

    for n in range(1, number + 1):
        factor = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factor += 1
                if i * i != n:
                    factor += 1

        if factor > limit:
            answer += power
        else:
            answer += factor

    return answer
