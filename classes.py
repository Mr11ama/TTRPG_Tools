from functions import roll_2D
from functions import DM

class Character:
    def __init__(self, name):
        self.name = name
        self.stats = self.Characteristics()
        self.DM = self.Characteristic_DMs(self.stats)
        self.skills = self.Skills()
        self.age = 18
        self.term = 1
        print("Name: ", self.name, "| Age: ", self.age)
        print("STR: ",self.stats.STR,"\nDEX: ",self.stats.DEX,"\nEND: ",self.stats.END,"\nINT: ",self.stats.INT,"\nEDU: ",self.stats.EDU,"\nSOC: ",self.stats.SOC)
        self.Pick_Background_Skills()

    class Characteristics:
        def __init__(self):
            self.STR = roll_2D(0)
            self.DEX = roll_2D(0)
            self.END = roll_2D(0)
            self.INT = roll_2D(0)
            self.EDU = roll_2D(0)
            self.SOC = roll_2D(0)

    class Characteristic_DMs:
        def __init__(self,stats):
            self.STR = DM(stats.STR)
            self.DEX = DM(stats.DEX)
            self.END = DM(stats.END)
            self.INT = DM(stats.INT)
            self.EDU = DM(stats.EDU)
            self.SOC = DM(stats.SOC)

    class Skills:
        def __init__(self):
            self.Admin = None
            self.Advocate = None
            self.Animals = None
            self.Art = None
            self.Astrogation = None
            self.Athletics = None
            self.Broker = None
            self.Carouse = None
            self.Deception = None
            self.Diplomat = None
            self.Drive = None
            self.Electronics = None
            self.Engineer = None
            self.Explosives = None
            self.Flyer = None
            self.Gambler = None
            self.Gunner = None
            self.Gun_Combat = None
            self.Heavy_Weapons = None
            self.Investigate = None
            self.Jack_of_All_Trades = None
            self.Language = None
            self.Leadership = None
            self.Mechanic = None
            self.Medic = None
            self.Melee = None
            self.Navigation = None
            self.Persuade = None
            self.Pilot = None
            self.Profession = None
            self.Recon = None
            self.Science = None
            self.Seafarer = None
            self.Stealth = None
            self.Steward = None
            self.Streetwise = None
            self.Survival = None
            self.Tactics = None
            self.Vacc_Suit = None

    def Pick_Background_Skills(self):
        Max_Background_Skills = self.DM.EDU + 3
        print(f"Based on your education up to now, you may pick {Max_Background_Skills} background skills",)
        i = 0
        while i < Max_Background_Skills:
            #print(Max_Background_Skills)
            i += 1






p1 = Character("Jimothy Jhalomet")
#print(p1.name, "STR: ",p1.stats.STR, "DM: ",p1.DM.STR)
#print(p1.skills.Admin)

