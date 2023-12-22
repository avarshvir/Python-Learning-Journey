class Student:


    def __init__(self, name, branch, age):
         self.name = name
         self.branch = branch
         self.age = age


    def get_value(self):
        print("name   ",self.name)
        print("age    ",self.age)
        print("branch ",self.branch)

s1 = Student("abc","cse",20)
s2 = Student("xyz","ece",21)
print(s1.name, s1.branch, s1.age)
print(s2.name)

s3 = Student("qwe","me",20)
s3.get_value()


