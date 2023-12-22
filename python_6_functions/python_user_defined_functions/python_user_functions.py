#creating simple function
def simple_function():
    print("this is my first function in python")

#calling simple function
simple_function()

#default argument function
print("Below is default argument function")
def def_arg_fun(n1, n2 =10):
    print("n1 : ",n1)
    print("n2 : ",n2)

def_arg_fun(5)
def_arg_fun("hello",20)

#keyword argument function
print("Below is keyword argument function")
def key_arg_fun(k1,k2):
    print("k1 : ",k1)
    print("k2 : ",k2)
print("without using keyword")
key_arg_fun(90,100)
print("using keyword")
key_arg_fun(k2=105,k1=60)

#arbitrary arugument *args
print("Below is arbitrary argument function")
def arb_arg_fun(*animal):
    print("animals : ",animal)
    print("animals : ",animal[:2])
arb_arg_fun("lion",1,"tiger",2,"cat",3)