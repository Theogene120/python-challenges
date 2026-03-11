from collections import Counter

s = input()
list = list(s)
list.sort()
string =''.join(list)

counter = Counter(string)
arr = []
for k,v in counter.items():
    arr.append([k,v])


arr.sort(key=lambda x:x[1], reverse=True)
i = 0
for k, v in arr:
    if i < 3:
        print(k, v)
        i = i + 1
