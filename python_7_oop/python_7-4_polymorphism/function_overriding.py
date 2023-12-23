class A:
    def abc_fun(self):
        print("Hello A")
class B(A):
    def abc_fun(self):
        print("Hello B")
class C(B):
    def abc_fun(self):
        print("Hello C")

c = C()
c.abc_fun()

b = B()
b.abc_fun()
