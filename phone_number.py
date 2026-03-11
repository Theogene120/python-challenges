n = int(input())
phone_book = {}
for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone
