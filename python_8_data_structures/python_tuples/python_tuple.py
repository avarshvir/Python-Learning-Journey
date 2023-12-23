#creating tuple
A_tuple = ('A',1,'B',5,'abc',6)

#accessing tuple element
print(A_tuple)
print(A_tuple[3])

#slicing
print(A_tuple[1:5])

#concatenation
B_tuple = ('C',7,'D',2)
C_tuple = A_tuple + B_tuple
print(C_tuple)

#updatation, removing and insertion in tuple not allowed as it non changeable
#but can be done by converting into list and then again converting into tuple
D_tuple =list(A_tuple)
D_tuple.append(7)
A_tuple = tuple(D_tuple)
print(A_tuple)

#repetition
E_tuple = 2*A_tuple
print(E_tuple)

#length of tuple
print(len(E_tuple))

#membership
is_present = 'A' in A_tuple
print(is_present)