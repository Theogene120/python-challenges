def swap(string):
    target = []
    for i in string:
        if i.isalpha() :
            if i.isupper():
                target.append(i.lower())
            else:
                target.append(i.upper())
        else:
            target.append(i)

    return ''.join(target)


print(swap('tHeos ig'))
print(swap('Www.HackerRank.com'))
print(swap('HackerRank.com presents "Pythonist 2"'))