nOFq = int(input())
writtenQ = 0

for _ in range(nOFq):
    q = list(map(int, input().split())) 

    counter = 0
    for v in q:
        if v == 1:
            counter += 1

    if counter >= 2:
        writtenQ += 1

print(writtenQ)
