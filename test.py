def test(nums):
    n = len(nums)
    i = 0
    j = 1
    while j < n:
        if nums[i] == nums[j]:
            nums[i] *= 2
            nums[j] = 0
        i += 1
        j += 1

    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)

    return nums
            
print(test([1,2,2,1,1,0]))
print(test([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))