# def hackerlandRadioTransmitters(x, k):
#     x = sorted(set(x))  # sort and remove duplicates
#     n = len(x)
#     transmitters = 0
#     i = 0

#     while i < n:
#         # leftmost uncovered house
#         start = x[i]

#         # place transmitter as far right as possible (start + k)
#         transmitter = start + k

#         # skip all houses within transmitter's placement range
#         while i < n and x[i] <= transmitter:
#             i += 1

#         # transmitter covers up to transmitter + k, skip those houses too
#         while i < n and x[i] <= transmitter + k:
#             i += 1

#         transmitters += 1

#     return transmitters

string = '1234'
arr = [int(num) for num in list(string)]

print(arr)
s = "".join(arr)
print(s)


