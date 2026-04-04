
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     if arr[-1] > arr[0] + arr[1]:
#         print('YES')
#     else:
#         print('NO')

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # Best case: 1 Elite player (biggest) vs 2 Crowd players (two smallest)
    if arr[-1] > arr[0] + arr[1]:
        print('YES')
    else:
        print('NO')
