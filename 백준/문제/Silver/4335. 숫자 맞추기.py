up_limit = 11
down_limit = 0
while True:
    n = int(input())
    if n == 0:
        break

    answer = input()
    if answer == "too high":
        if up_limit > n:
            up_limit = n
    elif answer == "too low":
        if down_limit < n:
            down_limit = n
    else:
        if not (down_limit < n < up_limit):
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        up_limit = 11
        down_limit = 0
