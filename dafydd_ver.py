from classes import Character
from functions import roll_2D

adventuring = False

player = Character("Jimothy Jhalomet")
print("Name: ", player.name, "| Age: ", player.age)
print("STR: ",player.stats.STR,"\nDEX: ",player.stats.DEX,"\nEND: ",player.stats.END,"\nINT: ",player.stats.INT,"\nEDU: ",player.stats.EDU,"\nSOC: ",player.stats.SOC)

while not adventuring:
    print("Do you want to stop character generation and start adventuring? Y/N")
    player_input = input()
    if player_input == "y":
        adventuring = True