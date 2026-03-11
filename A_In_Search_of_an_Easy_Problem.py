people = int(input())
ans = list(map(int, input().split()))
isHard = ''
for n in ans:
    if(n == 1):
        isHard = True
        break
 
if(isHard == True):
    print('HARD')
else:
    print('EASY')