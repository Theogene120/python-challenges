
dict = dict([('name','john'), ('age', 30), ('city', 'New York')])
sqr_dict = {num: num ** 2 for num in range(1, 11)}

print(dict)
print(sqr_dict)

age = dict['age']
print(age)

country = dict.get('country','Rwanda')
print(country)


print(dict)

dict['age'] = 20
dict['age'] = dict.get('age', 0) + 10

dict['age'] += 30

print(dict)
print('--------------------------------')

for key in dict:
    print (key)
print('--------------------------------')

for k in dict.items():
    print(k)
print('--------------------------------')
for value in dict.values():
    print(value)

print('--------------------------------')

dict2 = dict
print(dict2)
print('--------------------------------')

dict2['name'] = 'Daniel'
print(dict2)
print(dict)




print('--------------------------------')
print(dict3)
print(dict)
print('--------------------------------')


dict3 = dict.copy()

dict['members'] = [1,2,3]
dict2['members'] = [1,2,3]
dict3['members'] = [1,2,3]

dict3['members'].append(4)
print(dict)
print(dict2)
print(dict3)


