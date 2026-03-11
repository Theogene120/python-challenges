def removeDuplicates(nums):
        for i in nums:
            for j in nums:
                if i == j:
                     nums.remove(j)
        return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))
