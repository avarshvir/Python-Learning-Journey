class Fish:
    def __init__(self):
        print("This is non parameterized constructor")

    def get_fish(self,type):
        print("fish : ",type)

f1 = Fish()
f1.get_fish("dolphin")