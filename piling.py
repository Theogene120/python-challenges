tests = int(input())

for _ in range(tests):
    n = int(input())
    block = list(map(int, input().split()))

isFine = 'Yes'
i=0
for i in range(len(block)):
    if(block[i] > block[i + 1]):
        isFine = 'No'
        break

print("Yes")