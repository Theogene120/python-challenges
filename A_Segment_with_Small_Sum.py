n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
cur_sum = 0
max_ = 0
for end in range(len(nums)):
    cur_sum += nums[end]
    while cur_sum > s:
        cur_sum -= nums[start]
        start += 1
    max_ = max(max_, end - start + 1)

print(max_)