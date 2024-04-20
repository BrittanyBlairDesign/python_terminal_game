# File contains components for various classes to use in the game. 
# Components in file :
#     - Movement
#     - Stat

import vectors
import random

#### HANDLES THE LOCATION AND MOVEMENT OF CLASSES THAT ARE COMPOSED WITH IT ####
class Movement:
    def __init__(self, location:vectors.Vector2, direction:vectors.Vector2 = vectors.Vector2(0,0)) -> None:
        self.location = location
        self.direction = direction
    def __repr__(self) -> str:
        return "Location : " + str(self.location) + "\nDirection : " + str(self.direction)

#       Return the value of a variable   #
    def GetLocation(self):
        return self.location
    def GetDirection(self):
        return self.direction
    def GetPossibleDirections(self):
        dir_keys = []
        for i in self.directions.keys():
            dir_keys.append(i)
        return dir_keys
    
#       Set the value of the a Variable  #
    def SetLocation(self, newLocation: vectors.Vector2) -> None:
        self.location = newLocation
    def SetDirection(self, direction:str):
        if direction in self.directions.keys():
            self.direction = vectors.Vector2(self.directions[direction][0], self.directions[direction][1])
        else:
            UserWarning("{d} is not a valid direction to move in".format(d=str(direction)))
    
#       Game related Methods             #
    def Move(self) -> vectors.Vector2:
        self.location.x += self.direction.x
        self.location.y += self.direction.y
        print(self.location)
        return self.location
    
    def TestSurroundings(self) -> list[vectors.Vector2]:
        surroundings = []
        for d in self.directions.values():
            surroundings.append(self.direction + vectors.Vector2(d[0],d[1]))
        return surroundings
    
    ## Movement variables ##
    location: vectors.Vector2 = vectors.Vector2(0,0)
    direction: vectors.Vector2 = vectors.Vector2(0,0)
    directions = {"up": [-1, 0], "down": [1, 0],"right":[0, -1],"left": [0, 1]}
    
#### HANDLES THE  IFORMATION REGARDING A SPECIFIC STAT OF AN OBJECT ####
class Stat:
    def __init__(self, value: int | float, min_value: int | float = 1 , max_value: int | float = 0):
        self.value = value
        if value > max_value:
            self.max_value = value
        else:
            self.max_value = max_value
        self.min_value = min_value
        print(self)
    def __repr__(self) -> str:
        return "{x}/{y}".format(x=str(self.value),y=str(self.max_value))
#       Get the value of current stat variables   #
    def GetValue(self) -> int | float:
        return self.value
    def GetMax(self) -> int | float:
        return self.max_value
    def GetMin(self) -> int | float:
        return self.min_value
    
#       Make changes to the 'value' variable      #
    def Increase(self, x: int | float):
        if self.value + x <= self.max_value:
            self.value += x
        else:
            self.value = self.max_value
    def Decrease(self, x: int | float):
        if self.value - x > self.min_value:
            self.value -= x
        else:
            self.value = self.min_value
    def Reset(self):
        self.value = self.max_value

    ## Stat variables ##
    value: int | float
    min_value: int | float
    max_value: int | float


























