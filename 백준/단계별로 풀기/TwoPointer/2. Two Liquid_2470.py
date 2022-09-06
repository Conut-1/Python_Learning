import sys
input = sys.stdin.readline

def two_pointer():
    i = 0
    j = n - 1
    res = []
    minimum = float("inf")

    while i < j:
        if a[i] + a[j] == 0:
            return [a[i], a[j]]
        elif abs(a[i] + a[j]) < minimum:
            minimum = abs(a[i] + a[j])
            res = [a[i], a[j]]
        if a[i] + a[j] < 0:
            i += 1
        else:
            j -= 1

    return res


def find():
    if a[0] > 0:
        return [a[0], a[1]]
    elif a[-1] < 0:
        return [a[-2], a[-1]]
    else:
        return two_pointer()


n = int(input())
a = list(map(int, input().split()))

a.sort()

print(*find())



# def binary_search():
#     high = n - 1
#     low = 0
#     while low <= high:
#         mid = (high + low) // 2
#         if a[mid] < 0:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return mid


# def two_pointer():
#     search_res = binary_search()
#     if a[search_res] > 0:
#         acid, alkaline = search_res, search_res - 1
#     else:
#         acid, alkaline = search_res + 1, search_res

#     minimum = a[acid] + a[alkaline]
#     while acid < n and alkaline >= 0:
#         print()