

def moveZeroes(nums):
    n = len(nums)
    left = 0
    right = 1

    while right < n:
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        elif nums[left] != 0:
            left += 1
            right = left + 1
        else:
            right += 1
    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1]))
print(moveZeroes([1,0,1]))