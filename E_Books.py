n, t = map(int, input().split())
books = list(map(int, input().split()))

left = 0
window_sum = 0
max_len = 0

for right in range(n):
    window_sum += books[right]
    while window_sum > t:
        window_sum -= books[left]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)