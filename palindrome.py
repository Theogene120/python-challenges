def isPalindrome(self, x):
    if(x > 0):
        rev = str(x)[::-1]
    return int(rev) == x
print(isPalindrome(any, 121))