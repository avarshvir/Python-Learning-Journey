op = open('demo_file2.txt','r')
print(op.read())

#Read Only Parts of the File
op2 = open("demo_file2.txt", "rb")
print(op2.read(5))

#Read Lines
op3 = open("demo_file2.txt", "r+")
print(op3.readline())
print(op3.readline())

#Read by Looping
op4 = open('demo_file2.txt','rb+')
for i in op4:
    print(i)

op.close()
op2.close()
op3.close()
op4.close()
#print(op3.name)