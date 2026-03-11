string = []
for i in range(6):
    if(i % 3 == 0 and i % 5):
        string.append("FizzBuzz")
    elif(i % 3 == 0):
        string.append("Fizz")
    elif(i % 5 == 0):
        string.append("Buzz")
    else:
        string.append(i)

print(string)