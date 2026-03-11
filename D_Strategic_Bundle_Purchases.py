t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)  # most expensive first
    b.sort(reverse=True)  # largest coupons first

    total_cost = 0
    i = 0           # start of expensive items
    j = n - 1       # start of cheap items

    for coupon in b:
        # take `coupon` items
        # pay for coupon-1 most expensive (free = cheapest)
        total_cost += sum(a[i:i+coupon-1])  # pay for first coupon-1 items
        i += coupon - 1
        j -= 1  # free item comes from the end

    # add remaining items that were not in any coupon
    while i <= j:
        total_cost += a[i]
        i += 1

    print(total_cost)