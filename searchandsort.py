# def strStr(haystack, needle):
#     if needle not in haystack:
#         return -1
#     else:
#         return haystack.index(needle)

# print(strStr("sadbutsad", "sad"))
# print(strStr("leetcode", "leeto"))

def func(nums, target):

    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
print(func([1,3,5,6], 5))
print(func([1,3,5,6], 2))
        