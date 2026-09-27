class pub_mod:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        return
    def Name(self):
        print("Name:",self.name)
    def Age(self):
        print("Age:",self.age)
        return 
obj = pub_mod("Jason",35)
obj2 = pub_mod("Nene",15)
obj.Name()
obj.Age()
obj2.Name()
obj2.Age()