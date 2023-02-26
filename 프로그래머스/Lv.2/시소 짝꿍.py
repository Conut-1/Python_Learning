def solution(weights):

    def is_partner(a, b):
        if a == b:
            return True
        for i in range(2, 2 + 3):
            for j in range(2, 2 + 3):
                if a * i == b * j:
                    return True
        return False

    weight_map = dict()
    for weight in weights:
        if weight in weight_map:
            weight_map[weight] += 1
        else:
            weight_map[weight] = 1

    answer = 0
    weight_key = list(weight_map.keys())
    for i in range(len(weight_key)):
        for j in range(i, len(weight_key)):
            if is_partner(weight_key[i], weight_key[j]):
                if i == j:
                    answer += weight_map[weight_key[i]] * (weight_map[weight_key[i]] - 1) // 2
                else:
                    answer += weight_map[weight_key[i]] * weight_map[weight_key[j]]

    return answer
