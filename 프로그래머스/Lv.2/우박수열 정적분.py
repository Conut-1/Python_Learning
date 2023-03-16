def solution(k, ranges):
    seq = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        seq.append(k)

    area_prefix = [0]
    for i in range(len(seq) - 1):
        area_prefix.append((seq[i] + seq[i + 1]) / 2 + area_prefix[-1])

    answer = []
    for a, b in ranges:
        if a > len(seq) + b - 1:
            answer.append(-1)
        elif a == len(seq) + b - 1:
            answer.append(0)
        else:
            answer.append(area_prefix[b - 1] - area_prefix[a])

    return answer
