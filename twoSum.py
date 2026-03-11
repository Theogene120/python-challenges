class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j]  == target and i != j:
                    return i, j

obj = Solution()
print(obj.twoSum([3,2,4], 6))
print(obj.twoSum([2,7,11,15], 9))
