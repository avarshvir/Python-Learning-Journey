#creatng dictionary
a_dict = {
    'name':'python',
    'version':3,
    'year':1991
}
print(a_dict)

print("---------------------------------")

#accessing
x = a_dict['year']
print(x)
'''y = a_dict[3]
print(y)'''
print("---------------------------------")


#accessing by inbuilt methods
#get method
print(a_dict.get('name'))
print("---------------------------------")

#keys method
print(a_dict.keys())
print("---------------------------------")

#values method
print(a_dict.values())
print("---------------------------------")

#items method
print(a_dict.items())
print("---------------------------------")

#modifying or changing values
a_dict['version'] = 3.1
print(a_dict)
print("---------------------------------")

#adding new item or key pair values
a_dict['name of DS'] = 'tuple'
print(a_dict)
print("---------------------------------")

#removing items
a_dict.pop('name of DS')
print(a_dict)
#popitem() will remove last item in tuple
#del a_dict
#print(a_dict)
#print(a_dict.clear())
print("---------------------------------")

#looping in dictionary
for i in a_dict:
    print(a_dict[i])
print("---------------------------------")

for j in a_dict:
    print(j)
print("---------------------------------")

#copy dictionary
b_dict = a_dict.copy()
print(b_dict)
print("---------------------------------")

