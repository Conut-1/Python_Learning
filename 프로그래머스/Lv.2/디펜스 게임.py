import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    damage = 0
    for e in enemy:
        heapq.heappush(heap, e)
        if len(heap) > k:
            damage += heapq.heappop(heap)
            if damage > n:
                break
        answer += 1
    return answer
