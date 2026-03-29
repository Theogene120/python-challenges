import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
for num in b:
    result.append(bisect.bisect_left(a, num))

print(*result)