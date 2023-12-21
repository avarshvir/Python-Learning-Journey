fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


a = [1,2,3,4,5,6,7,8,9]
print("1st for loop")
for i in a[:4]:
    print(a)
print("2nd for loop")
for i in a[:4]:
    print(i)
print("3rd for loop")
for i in range(len(a)):
    print(a)
print("4th for loop")
for i in range(len(a)):
    print(i)


print("Range function")
print(range(15))

print(list(range(15)))

print(list(range(4, 9)))

print(list(range(5, 25, 4)))