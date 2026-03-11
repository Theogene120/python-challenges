
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[-1] > arr[0] + arr[1]:
        print('YES')
    else:
        print('NO')

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     arr.sort()

#     elite_sum = 0
#     crowd_sum = 0

#     i = n - 1   # largest
#     j = 0       # smallest

#     elite_count = 0
#     crowd_count = 0

#     while j < i:
#         elite_sum += arr[i]
#         elite_count += 1
#         i -= 1

#         crowd_sum += arr[j]
#         crowd_count += 1
#         j += 1

#         if elite_sum > crowd_sum and elite_count < crowd_count:
#             print("YES")
#             break
#     else:
#         print("NO")


    # if n % 2 == 1:
    #     portion = n // 2
    #     if sum(arr[0:portion]) > sum((arr[portion:])):
    #         print('YES')
    #     else:
    #         print('NO')
    # else:
    #     portion = int(n / 2 - 1)
    #     if sum(arr[0:portion]) > sum((arr[portion:])):
    #         print('YES')
    #     else:
    #         print('NO')


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     arr.sort()

#     left_sum = 0
#     right_sum = sum(arr)

#     for i in range(n):
#         left_sum += arr[i]
#         right_sum -= arr[i]

#         if (i + 1) < (n - (i + 1)) and left_sum < right_sum:
#             print("YES")
#             break
#     else:
#         print("NO")