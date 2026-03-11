def Twosum(numbers, target):

    n = len(numbers)
    left = 0
    right = n - 1
    
    while right > 0:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1

print(Twosum([2,7,11,15], 9))