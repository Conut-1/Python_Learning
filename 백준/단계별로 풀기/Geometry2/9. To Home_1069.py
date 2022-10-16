def solve():
    X, Y, D, T = map(int, input().split())

    distance = (X ** 2 + Y ** 2) ** 0.5
    if (T > D):
        return distance
    jump_count = distance // D
    distance -= jump_count * D
    time = jump_count * T
    return time + min(distance, T + abs(distance - D), 2 * T if jump_count ==0 else T)

print(solve())
