
def maxSum(nums,k):
    max_ = float('-inf')
    start = 0
    cur_sum = 0
    for end in range(len(nums)):
        cur_sum += nums[end] 

        if (end - start + 1) == k:
            max_ = max(max_, cur_sum)
            cur_sum -= nums[start]
            start += 1
    return max_/k


print(maxSum([1,12,-5,-6,50,3], 4))           