from functions import roll_2D



class Character:
    def __init__(self, name):
        self.name = name
        self.stats = self.Characteristics()
        self.age = 18
        self.term = 1
    
    class Characteristics:
        def __init__(self):
            self.STR = roll_2D(0)
            self.DEX = roll_2D(0)
            self.END = roll_2D(0)
            self.INT = roll_2D(0)
            self.EDU = roll_2D(0)
            self.SOC = roll_2D(0)

    

    





p1 = Character("Jimothy Jhalomet")
print(p1.name, p1.stats.STR)

