# File contains components for various classes to use in the game. 
# Components in file :
#     - Movement
#     - Stat

import vectors
import random

#### HANDLES THE LOCATION AND MOVEMENT OF CLASSES THAT ARE COMPOSED WITH IT ####
class Movement:
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return "Location :" + self.location + "\nDirection : " + self.direction

#       Return the value of a variable   #
    def GetLocation(self) -> vectors.Vector2:
        return self.location
    def GetDirection(self) -> vectors.Vector2:
        return self.direction
    def GetPossibleDirections(self) -> list[str]:
        return self.directions.keys()
    
#       Set the value of the a Variable  #
    def SetLocation(self, newLocation: vectors.Vector2) -> None:
        self.location = newLocation
    def SetLocation(self, x: float| int , y: float|int) -> None:
        self.location.x = x
        self.location.y = y
    def setDirection(self, direction:str):
        if direction in self.directions.keys():
            new_direction = vectors.Vector2(self.directions[direction][0], self.directions[direction][1])
        else:
            UserWarning("{d} is not a valid direction to move in")
    
#       Game related Methods             #
    def Move(self) -> vectors.Vector2:
        self.location += self.direction
        return self.location
    def MoveRandom(self) -> vectors.Vector2:
        self.Location += random.choice(self.directions.keys())
    def TestSurroundings(self) -> list[vectors.Vector2]:
        surroundings = []
        for d in self.directions.values():
            surroundings.append(self.direction + vectors.Vector2(d[0],d[y]))
        return surroundings
    
    ## Movement variables ##
    location: vectors.Vector2 = vectors.Vector2(0,0)
    direction: vectors.Vector2 = vectors.Vector2(0,0)
    directions: dict[str, list[int]] = {"up":   [-1, 0],
                  "down": [1, 0],
                  "right":[0, -1],
                  "left": [0, 1]}
    
#### HANDLES THE  IFORMATION REGARDING A SPECIFIC STAT OF AN OBJECT ####
class Stat:
    def __init__(self):
        self.value = 1
        self.max_value = 1
        self.min_value = 0
    def __init__(self, value: int | float):
        self.value = value
        self.max_value = value
        self.min_value = value
    def __init__(self, min_value: int | float, max_value: int | float):
        self.value = max_value
        self.max_value = max_value
        self.min_value = min_value
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
        self.value = max

    ## Stat variables ##
    value: int | float
    min_value: int | float
    max_value: int | float


























