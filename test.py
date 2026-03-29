# def palindromeIndex(s):
#     if s == s[::-1]:
#         return -1
    
#     left = 0
#     right = len(s) - 1
    
#     while left < right:
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             # remove right
#             if s[left+1:right+1] == s[left+1:right+1][::-1]:
#                 return left
#             # r4move left
#             else:
#                 return right
    
#     return -1

# print(palindromeIndex('bcbc'))  # 0 or 3
# print(palindromeIndex('aaab'))  # 3

def pairs(k, arr):
    arr.sort()
    count = 0
    left, right = 0, 1
    
    while right < len(arr):
        diff = arr[right] - arr[left]
        if diff == k:
            count += 1
            left += 1
            right += 1
        elif diff < k:
            right += 1
        else:
            left += 1
        if left == right:
            right += 1
    
    return count

print(pairs(1, [1,2,3,4]))
print(pairs(2, [1,5,3,4,2])) # 3


def beautifulTriplets(d, arr):
    arr.sort()
    count = 0
    
    for i in range(len(arr) - 2):
        if arr[i+1] - arr[i] == d and arr[i+2] - arr[i+1] == d:
            count += 1
    
    return count

print(beautifulTriplets(1, [2,2,3,4,5]))  # 4

print(beautifulTriplets(1, [2,2,3,4,5]))