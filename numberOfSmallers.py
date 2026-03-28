def smallerNumbersThanCurrent(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] < nums[i]:
                count += 1
        ans.append(count)
    return ans

print(smallerNumbersThanCurrent([8,1,2,2,3]))


