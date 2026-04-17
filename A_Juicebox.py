
t = int(input())

for _ in range(t):

    # n - number of shelves
    # k - number of juice boxes
    n, k = map(int, input().split())

    brand_sum = [0] * (k+1)

    for _ in range(k):
        b, c = map(int, input().split())
        brand_sum[b] += c

    brand_sum.sort(reverse=True)


    print(sum(brand_sum[:n]))
    