# def moveZeroes(nums):
#     count = 0
#     for num in nums:
#         if num == 0:
#             #del nums[idx]
#             nums.remove(num)
#             count += 1
            
#         for _ in range(count):
#             nums.append(0)

#     return nums

# print(moveZeroes([0,1,0,3,12]))
# print(moveZeroes([0,0,1]))

def moveZeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)
    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1]))