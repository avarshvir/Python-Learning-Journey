class Bird:
    def __init__(self,type):
        self.type = type
    def get_bird(self):
        print("Bird : ",self.type)

b1 = Bird("eagle")
b1.get_bird()