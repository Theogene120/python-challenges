import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    events = []

    for x in a:
        events.append((x+1, 1))
        events.append((x+n+1, -1))

    events.sort()

    cur = 0
    ans = 0

    for _, v in events:
        cur += v
        ans = max(ans, cur)

    print(ans)