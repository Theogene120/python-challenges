
def maxScoreIndices(nums):
    size = len(nums)
    
    # Suffix 1s count
    r_score = [0] * (size + 1)
    for i in range(size - 1, -1, -1):
        r_score[i] = r_score[i + 1] + (1 if nums[i] == 1 else 0)
    
    # Prefix 0s count
    l_score = [0] * (size + 1)
    for i in range(size):
        l_score[i + 1] = l_score[i] + (1 if nums[i] == 0 else 0)
    
    # Combine and find max
    result = [l_score[i] + r_score[i] for i in range(size + 1)]
    max_score = max(result)
    
    return [i for i, v in enumerate(result) if v == max_score]