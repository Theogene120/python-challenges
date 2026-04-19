t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = []

    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)

    b = []

    for i in range(n):
        for j in range(m):
            b.append(a[i][j])

    print(b)