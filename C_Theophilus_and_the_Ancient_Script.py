# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     arr_s = list(s)
 
#     i = 0
#     j = 1
#     counter = 0
#     for i in range(len(arr_s)):
#         for j in range(len(arr_s)):
#             if arr_s[i] == 'A' and arr_s[j] == 'B':
#                 arr_s[i], arr_s[j] = arr_s[j], arr_s[i]
#                 counter += 1
#     print(counter)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    first_a = -1
    for i in range(n):
        if s[i] == 'A':
            first_a = i + 1
            break

    if first_a == -1:
        print(0)
    else:
        print(n - first_a)
