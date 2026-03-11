def counter(nums, k):
    n = len(nums)
    left = 0
    right = n - 1
    count = 0
    while right >= 0:
        if nums[left] == nums[right] and left*right % k == 0:
            count += 1
        left += 1
        right -= 1
    return count
    
print(counter([3,1,2,2,2,1,3], 2))