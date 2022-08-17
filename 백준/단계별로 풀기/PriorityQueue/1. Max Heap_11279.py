import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    inst = int(input())
    if inst == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-inst, inst))


# import sys
# input = sys.stdin.readline


# heap = [0] * 100001
# n = int(input())
# size = 0
# for _ in range(n):
#     inst = input().rstrip()
#     if inst == "0":
#         if size == 0:
#             print(0)
#         else:
#             print(heap[1])
#             tmp = heap[size]
#             index = 1
#             size -= 1
#             while index <= size:
#                 if index * 2 > size:
#                     break
#                 elif index * 2 == size:
#                     if heap[index * 2] > tmp:
#                         heap[index] = heap[index * 2]
#                         index *= 2
#                 else:
#                     if heap[index * 2] > tmp or heap[index * 2 + 1] > tmp:
#                         if heap[index] > heap[index * 2] + 1:
#                             heap[index] = heap[index * 2]
#                             index = index * 2
#                         else:
#                             heap[index] = heap[index * 2 + 1]
#                             index = index * 2 + 1
#             heap[index] = tmp
#     else:
#         size += 1
#         index = size
#         tmp = int(inst)
#         while index != 1 and tmp > heap[index // 2]:
#             heap[index] = heap[index // 2]
#             index //= 2
#         heap[index] = tmp
