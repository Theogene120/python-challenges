def longest(s):
    visited = set()
    start = 0
    largest = 0
    
    for end in range(len(s)):
        while s[end] in visited:
            visited.remove(s[start])
            start += 1
        visited.add(s[end])
        largest = max(largest, end-start+1)
    return largest

print(longest('abcbad'))