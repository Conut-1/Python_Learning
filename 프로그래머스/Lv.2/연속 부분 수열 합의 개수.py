def solution(elements):
    def get_sum(start, size):
        if start + size <= n:
            return prefix[start + size] - prefix[start]
        else:
            return (prefix[-1] - prefix[start]) + (prefix[start + size - n] - prefix[0])

    num_set = set()
    n = len(elements)
    prefix = [0]
    for e in elements:
        prefix.append(prefix[-1] + e)

    for i in range(n):
        for j in range(1, n + 1):
            num_set.add(get_sum(i, j))

    return len(num_set)
