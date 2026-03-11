def missingNumber(nums):
    nums.sort()
    i = 0
    for num in range(1, nums[-1] + 1):
        if(num != nums[num]):
            return num

print(missingNumber([3,0,1]))