def solution(n, l, r):

    def count_cantor(n, idx):
        if idx == 0:
            return 0
        if idx == 5 ** n:
            return 4 ** n
        
        count = 0
        while n:
            idx %= 5 ** n
            n -= 1
            size = 5 ** n
            if idx < size:
                continue
            count += 4 ** n
            if idx < size * 2:
                continue
            count += 4 ** n
            if idx < size * 3:
                break
            if idx < size * 4:
                continue
            count += 4 ** n
            if idx < size * 5:
                continue
            count += 4 ** n
        return count

    answer = count_cantor(n, r) - count_cantor(n, l - 1)
    return answer
