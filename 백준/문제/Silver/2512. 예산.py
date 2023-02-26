def search():
    start = 0
    end = provinces[-1]

    if sum(provinces) <= M:
        return provinces[-1]
    while start <= end:
        mid = (start + end) // 2
        budget = 0
        for province in provinces:
            if province < mid:
                budget += province
            else:
                budget += mid
        if budget == M:
            return mid
        elif budget < M:
            start = mid + 1
        else:
            end = mid - 1

    return end

N = int(input())
provinces = list(map(int, input().split()))
M = int(input())

provinces.sort()
print(search())
