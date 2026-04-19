n = int(input())
t = list(map(int, input().split()))

l, r = 0, n - 1
alice_time = 0
bob_time = 0
a, b = 0, 0

while l <= r:
    if alice_time <= bob_time: 
        alice_time += t[l]
        l += 1
        a += 1
    else:       
        bob_time += t[r]
        r -= 1
        b += 1

print(a, b)