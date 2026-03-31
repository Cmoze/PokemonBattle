"""
Cameron Chrisopher 
Zackery Schaub
Carter Moser
Sun MARCH 29, 2025

The purpose of this assignment is to practice the syntax of classes and creating objects. 

You will create 3 Pokemon objects, and 9 Move objects. If youve never heard of or played Pokémon, they are popular fictional creatures that learn “moves” which are attacks or abilities that they perform. Pokémon and moves have elemental types, like “Fire”, “Water”, “Grass”, and “Normal”.

In this assignment you will just create the objects (with their attributes and methods), 
and practice putting the objects in lists and accessing their attributes and methods. 
However, during the group project, you will have the objects interact with each other in a “battle”. 
You dont have to have any prior knowledge of Pokémon to do this assignment and the upcoming project, 
but it may help you to watch this clip for an idea of what Pokémon interactions are like:

You will put your code in the a08_pokemon_and_move_classes.py file. Do not edit or delete any other files.
"""
import random

# Move class
class Move() :
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points) :
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info(self) :
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"
    
    def generate_attack_value(self) :
        return random.randint(self.low_attack_points, self.high_attack_points)
    

# Creating 9 Move objects (fixed Tackle values only)
oTackle = Move("Tackle", "Normal", 5, 20)
oQuickAttack = Move("Quick Attack", "Normal", 6, 25)
oSlash = Move("Slash", "Normal", 10, 30)
oFlamethrower = Move("Flamethrower", "Fire", 5, 30)
oEmber = Move("Ember", "Fire", 10, 20)
oWaterGun = Move("Water Gun", "Water", 5, 15)
oHydroPump = Move("Hydro Pump", "Water", 20, 25)
oVineWhip = Move("Vine Whip", "Grass", 10, 25)
oSolarBeam = Move("Solar Beam", "Grass", 18, 27)

# List of moves
lMoveList = [oTackle, oQuickAttack, oSlash, oFlamethrower, oEmber, oWaterGun, oHydroPump, oVineWhip, oSolarBeam]

# Loop 
for moves in range(0, 3):
    iLength = len(lMoveList)
    iMoveNum = random.randrange(0, iLength)

    selected_move = lMoveList[iMoveNum]

    print(selected_move.get_info())
    print("Generated attack value:", selected_move.generate_attack_value())

    lMoveList.pop(iMoveNum)


# Pokemon class
class Pokemon():
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points
        #Extra
        self.moves = []

    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"

    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")
    #Extra practice
    def add_move(self, move):  
        self.moves.append(move)
    


input("Press enter to continue...")


# Create Pokemon objects
oBulbasaur = Pokemon("Bulbasaur", "Grass", 60)
oCharmander = Pokemon("Charmander", "Fire", 55)
oSquirtle = Pokemon("Squirtle", "Water", 65)

#Add specific moves to pokemon(extra):
oBulbasaur.add_move(oTackle)
oBulbasaur.add_move(oVineWhip)
oBulbasaur.add_move(oSolarBeam)
oBulbasaur.add_move(oSlash)
 
oCharmander.add_move(oQuickAttack)
oCharmander.add_move(oEmber)
oCharmander.add_move(oFlamethrower)
oCharmander.add_move(oSlash)
 
oSquirtle.add_move(oTackle)
oSquirtle.add_move(oWaterGun)
oSquirtle.add_move(oHydroPump)
oSquirtle.add_move(oSlash)

# Test Charmander
print(oCharmander.get_info())
oCharmander.heal()
print(oCharmander.get_info())

# List of Pokemon
lPokemonList = [oBulbasaur, oCharmander, oSquirtle]

# Loop through Pokemon
for pokemon in lPokemonList:
    print(pokemon.get_info())
    #This was so I contributed..
    print("  Moves:", [move.move_name for move in pokemon.moves])