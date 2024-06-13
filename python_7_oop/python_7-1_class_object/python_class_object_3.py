class Bird:
    def __int__(self,name, voice):
        self.name = name
        self.voice = voice

    def getBird(self):
        print(self.name)
        print(self.voice)

b = Bird()
b.__int__("Peacock","Mayur..")
b.getBird()