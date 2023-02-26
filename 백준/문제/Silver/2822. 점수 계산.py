scores = [(int(input()), i) for i in range(8)]
scores.sort(reverse=True)

final_score = 0
cases = []
for score, case in scores[:5]:
    final_score += score
    cases.append(case + 1)
cases.sort()

print(final_score)
print(*cases)
