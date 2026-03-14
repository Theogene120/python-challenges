def relative(arr1, arr2):

    ans = []
    remainder = []

    for num2 in arr2:
        for num1 in arr1:
            if num1 == num2:
                ans.append(num1)

    for n in arr1:
        if n not in ans:
            remainder.append(n)
    
    remainder.sort()
    return ans + remainder

print(relative([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))