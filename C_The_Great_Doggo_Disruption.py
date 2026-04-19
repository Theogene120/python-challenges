# from collections import Counter

# t = int(input())
# s = input()


# dict_s = Counter(s)
# for v in dict_s.values():
#     if v >= 2:
#         print('Yes')
#         break
# else:
#     print('No')
    

from collections import Counter
n = int(input())
s = input()
s.lower
if n == 1:
    print("Yes")
else:
    freq = Counter(s)
    if any(v >= 2 for v in freq.values()):
        print("Yes")
    else:
        print("No")
