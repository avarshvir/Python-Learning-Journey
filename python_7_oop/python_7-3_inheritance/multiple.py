class Add:
    def add_fun(self,a,b):
        return a+b
class Sub:
    def sub_fun(self,a,b):
        return a-b
class Div(Add,Sub):
    def div_fun(self,a,b):
        return a/b

a1 = Div()
print(a1.add_fun(5,4))
print(a1.sub_fun(5,1))
print(a1.div_fun(5,2))