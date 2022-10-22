hour, minute = map(int, input().split())
time = int(input())

hour += (minute + time) // 60
minute = (minute + time) % 60
hour %= 24

print(hour, minute)
