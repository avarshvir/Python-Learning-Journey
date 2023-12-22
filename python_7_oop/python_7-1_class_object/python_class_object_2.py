class Animal:
    def __init__(self,name,type,num):
        self.name = name
        self.type = type
        self.num = num

    def get_values(self):
        print("Name of animal : ",self.name)
        print("Type of animal : ",self.type)
        print("Quantity       : ",self.num)

a1 = Animal("Rob","Lion",21000)
a1.get_values()