def dividePlayers(skill):
    total = sum(skill)
    n = len(skill)
    teamSum = (total / n) * 2
    i=0
    j=1
    res =0
    count =0
    while j<n:
        s = skill[i] +skill[j]
        #print(skill[i], skill[j])

        if s == teamSum:
            count+=1
            res +=skill[i]*skill[j]
            if j-i ==1:
                i+=2
                j = i +1
            else :
                i +=1
                j = i +1
        else :
            j+=1
    print(res)
    if count == (n/2) :
        return res
    else :
        return -1

# print(dividePlayers([3,2,5,1,3,4]))
# print(dividePlayers([5,3,7,1]))
print(dividePlayers([5,4,1,1,5,2]))




    