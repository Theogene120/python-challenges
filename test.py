# import math
# def test(d, arr):
#     count = 0
#     size = len(arr)

#     for left in range(size):
#         for right in range(size):
#             if arr[right] - arr[left] == d and left < right:
#                 left = right
#                 count += 1
#     return math.ceil(count / 3)

# print(test(1, [2,2,3,4,5]))
# print(test(3, [1,2,4,5,7,8,10]))
# print(test(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]))



def sum_digits(a: str, b: str) -> str:
    result = []
    max_len = max(len(a), len(b))

    for i in range(max_len):
        digit_a = int(a[i])          if i < len(a) else None
        digit_b = int(b[-(i + 1)])   if i < len(b) else None

        if digit_a is not None and digit_b is not None:
            result.append(str(digit_a + digit_b))
        elif digit_a is not None:
            result.append(str(digit_a))
        else:
            result.append(str(digit_b))

    return "".join(result)


# Tests
print(sum_digits("99",   "99"))    # "1818"
print(sum_digits("123",  "45"))    # "1" + (2+5) + (3+4) → "179"  (1 alone, 7, 9) → Wait: b reversed = "54"
                                   # i=0: a[0]=1, b[-1]=5 → 6
                                   # i=1: a[1]=2, b[-2]=4 → 6
                                   # i=2: a[2]=3, no b    → 3  → "663"
print(sum_digits("5",    "123"))   # i=0: a[0]=5, b[-1]=3 → 8
                                   # i=1: no a,   b[-2]=2 → 2
                                   # i=2: no a,   b[-3]=1 → 1  → "821"
print(sum_digits("9",    "9"))     # "18"