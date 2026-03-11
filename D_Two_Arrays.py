t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))

    arr = list_n + list_m
    arr.sort()
    