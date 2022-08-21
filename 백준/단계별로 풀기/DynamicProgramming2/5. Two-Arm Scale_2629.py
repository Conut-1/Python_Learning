weight_num = int(input())
weights = list(map(int, input().split()))
bead_num = int(input())
beads = list(map(int, input().split()))

dp = set()
for weight in weights:
    tmp_arr = list(dp)
    for possible_weight in tmp_arr:
        dp.add(abs(weight - possible_weight))
        dp.add(weight + possible_weight)
    dp.add(weight)

res = []
dp = list(dp)
sum = sum(weights)
res_arr = ["N"] * (sum + 1)
for possible_weight in dp:
    res_arr[possible_weight] = "Y"
for bead in beads:
    if bead > sum:
        res.append("N")
    else:
        res.append(res_arr[bead])

print(*res)
