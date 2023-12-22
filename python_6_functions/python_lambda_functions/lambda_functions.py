add = lambda a:a+9
print(add(4))

def sub(n):
    return lambda b:b*n

c = sub(5)
print(c(3))

d = lambda a,b,c:a+b+c
print((d(10,20,30)))
