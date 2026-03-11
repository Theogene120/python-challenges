n = int(input())
list = [input().strip() for _ in range(n)]
for word in list:
    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)


