import sys
input = sys.stdin.readline

while True:
    try:
        n, *arr = map(int, input().split())
    except:
        break
    jolly = set([i for i in range(1, n)])

    for i in range(n - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff in jolly:
            jolly.remove(diff)

    if len(jolly):
        print("Not jolly")
    else:
        print("Jolly")
