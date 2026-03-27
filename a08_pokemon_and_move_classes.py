"""
The purpose of this assignment is to practice the syntax of classes and creating objects. 

You will create 3 Pokemon objects, and 9 Move objects. If you’ve never heard of or played Pokémon, they are popular fictional creatures that learn “moves” which are attacks or abilities that they perform. Pokémon and moves have elemental types, like “Fire”, “Water”, “Grass”, and “Normal”.

In this assignment you will just create the objects (with their attributes and methods), and practice putting the objects in lists and accessing their attributes and methods. However, during the group project, you will have the objects interact with each other in a “battle”. You don’t have to have any prior knowledge of Pokémon to do this assignment and the upcoming project, but it may help you to watch this clip for an idea of what Pokémon interactions are like:

You will put your code in the a08_pokemon_and_move_classes.py file. Do not edit or delete any other files.
"""
import random

#Move class to give attributes to a move, and functions to return info about that move and generate a random number of attack points within the given range
class Move() :
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points) :
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points


    #Returns a string with the move_name, elemental_type, and the low_attack_points and high_attack_points.
    def get_info(self) :
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"
    
    #returns an int of a randomly generated number between the low_attack_points, and the high_attack_points of the move.
    def generate_attack_value(self) :
        return random.randint(self.low_attack_points, self.high_attack_points)
    


#Creating 9 objects for the moves used in this battle simulator
oTackle = Move("Tackle", "Normal", 5, 10)
oQuickAttack = Move("Quick Attack", "Normal", 6, 25)
oSlash = Move("Slash", "Normal", 10, 30)
oFlamethrower = Move("Flamethrower", "Fire", 5, 30)
oEmber = Move("Ember", "Fire", 10, 20)
oWaterGun = Move("Water Gun", "Water", 5, 15)
oHydroPump = Move("Hydro Pump", "Water", 20, 25)
oVineWhip = Move("Vine Whip", "Grass", 10, 25)
oSolarBeam = Move("Solar Beam", "Grass", 18, 27)

#List to contain all the moves
lMoveList = [oTackle, oQuickAttack, oSlash, oFlamethrower, oEmber, oWaterGun, oHydroPump, oVineWhip, oSolarBeam]

#Loop to select 3 moves (RANDOMLY) and display info about them, then removing them from the list to not allow repeats
for moves in range(0, 3):
    #This is to ensure that when an item from the list is removed, the loop doens't return an error if a number is selected out of range
    iLength = len(lMoveList)
    iMoveNum = random.randrange(0, iLength)
    print(Move.get_info(lMoveList[iMoveNum]))
    print("Generated attack value: " + str(Move.generate_attack_value(lMoveList[iMoveNum])))
    lMoveList.pop(iMoveNum)

#Pokemon class to get info, hit points, and an ability to heal
class Pokemon() :
    def __init__(self, name, elemental_type, hit_points,) :
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    #returns a string with the name, elemental_type and hit_points
    def get_info(self) :

    #adds 15 hit points to hit_points and prints out a message with the new number of hit_points. Shouldn't return anything.
    def heal(self) :
        return False










input("Press enter to continue...")