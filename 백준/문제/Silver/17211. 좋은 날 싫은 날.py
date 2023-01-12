N, mood = map(int, input().split())
mood_change = list(map(float, input().split()))

bad = mood
good = 1 - mood
for _ in range(N):
    bad, good = mood_change[1] * good + mood_change[3] * bad, mood_change[0] * good + mood_change[2] * bad

print(int(good * 1000))
print(int(bad * 1000))
