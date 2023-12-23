my_list = ['apple','mango','banana','cherry']
new_list = [x for  x in my_list if 'a' in x]
print(new_list)
my_list2 = [1,2,3,4,5,6]
new_list2 = [x**2 for x in my_list2]
print(new_list2)
new_list3 = [x for x in my_list if x!='apple']
print(new_list3)
new_list4 = [x for x in my_list if x=='apple']
print(new_list4)