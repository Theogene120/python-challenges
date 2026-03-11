
# n = int(input())
# arr = list(map(int, input().split()))
# s = []
# d = []
    
# arr.sort()

# for i in range(len(arr)):
#     if i %  2 == 0:
#         s.append(arr[i])
#     else:
#         d.append(arr[i])

# print(sum(s), sum(d))


n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
s = 0
d = 0
turn = 0

while left <= right:
    if arr[left] > arr[right]:
        card = arr[left]
        left += 1
    else:
        card = arr[right]
        right -= 1

    if turn % 2 == 0:
        s += card
    else:
        d += card

    turn += 1

print(s, d)

