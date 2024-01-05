j_scores = list(map(int, input().split()))
s_scores = list(map(int, input().split()))

res = "No"
j_score = 0
s_score = 0
for i in range(9):
    j_score += j_scores[i]
    if j_score > s_score:
        res = "Yes"
    s_score += s_scores[i]
print(res)
