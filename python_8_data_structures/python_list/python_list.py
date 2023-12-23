#creatint a list
A_list = ['a','b','c','d','e']
print(A_list)

#accessing list element
a1 = A_list[0]
b1 = A_list[2]
print(a1,b1)
print(A_list[4])

#slicing list
a2 = A_list[1:4]
print(a2)
print(A_list[:3])
print(A_list[-3:-1])

#appending and extending list
A_list.append('f')
print(A_list)

B_list = ['g','h']
A_list.extend(B_list)
print(A_list)
B_list.extend(A_list)
print(B_list)

#inserting element
A_list.insert(2,'b1')
print(A_list)

#removing element via value and index
A_list.remove('b1')
print(A_list)

A_list.pop(6)
print(A_list)

#finding index of an element
index = A_list.index('c')
print(index)

#checking if the element in the list or not
print('a' in A_list)
print('k' in A_list)

#length of list
print(len(A_list))

#sorting and reversing list
C_list = [0,4,1,4,6,2]
C_list.reverse()
print(C_list)
C_list.sort(reverse=True)
print(C_list)
C_list.sort()
print(C_list)

#looping in list
for i in A_list:
    print(i)

for j in range(len(B_list)):
    print(B_list[j])
    print(j)

#copy list
D_list = A_list.copy()
print(D_list)
E_list = D_list + C_list
print(E_list)


