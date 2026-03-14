def sortPeople(names, heights):
    n = len(names)

    for i in range(n):
        for j in range(n-i-1):
            if heights[j] < heights[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
                heights[j], heights[j+1] = heights[j+1], heights[j]
  
        return names
    
print(sortPeople(["Mary","John","Emma"], [180,165,170]))
print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))