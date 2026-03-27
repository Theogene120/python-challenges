def maximum(piles):
    piles.sort()
    n = len(piles)
    res = 0
    for i in range(n//3, n, 2):
        res += piles[i]
    return res

print(maximum([2,4,1,2,7,8]))