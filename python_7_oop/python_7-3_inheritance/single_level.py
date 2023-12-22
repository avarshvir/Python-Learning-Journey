class Employee:
    def employee(self,name,id):
        self.name = name
        self.id = id

class Developer(Employee):
    def developer(self,skills, grade, salary):
        self.skills = skills
        self.grade = grade
        self.salary = salary

    def display(self):
        print("name   : ",self.name)
        print("id     : ",self.id)
        print("skills : ",self.skills)
        print("grade  : ",self.grade)
        print("salary : ",self.salary)

d1 = Developer()
d1.employee("abc",121)
d1.developer("python",'A+',2000000)
d1.display()