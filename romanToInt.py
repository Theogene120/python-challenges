def romanToInt(s):
    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ans = 0
    prev = 0
    
    for letter in reversed(s):
        curr = numbers[letter]
        if curr < prev:
            ans -= curr
        else:
            ans += curr
        prev = curr

    return ans
        
print(romanToInt('XXVII'))
print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV")) # 1994

