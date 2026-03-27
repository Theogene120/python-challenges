
from collections import Counter

def findAnagrams(s, p):
    p_count = Counter(p)
    window = Counter(s[:len(p)])
    res = []
    
    if window == p_count:
        res.append(0)
    
    for right in range(len(p), len(s)):
        left = right - len(p)
        window[s[right]] += 1
        window[s[left]] -= 1
        
        if window == p_count:
            res.append(left + 1)
    
    return res

print(findAnagrams("cbaebabacd", "abc")) 
print(findAnagrams("abab", "ab"))   