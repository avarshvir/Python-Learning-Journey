class A:
    def a_fun(self):
        print("This is A")

class B(A):
    def b_fun(self):
        print("This is B")

class C(B):
    def c_fun(self):
        print("This is C")

c1 = C()
c1.a_fun()
c1.b_fun()
c1.c_fun()