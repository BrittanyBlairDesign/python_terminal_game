# File contains components for various classes to use in the game. 
# Components in file :
#     - Movement
#     - Stat

import vectors as v
import random

#### HANDLES THE LOCATION AND MOVEMENT OF CLASSES THAT ARE COMPOSED WITH IT ####
class Movement:
    def __init__(self, location:v.Vector2, direction:v.Vector2 = v.Vector2(0,0)) -> None:
        self.location = location
        self.direction = direction
    def __repr__(self) -> str:
        return "Location : " + str(self.location) + "\nDirection : " + str(self.direction)

#       Return the value of a variable   #
    def GetLocation(self):
        return self.location
    def GetDirection(self):
        return self.direction
    def GetPossibleDirections(self, map_size):
        dir_keys = []
        for i in self.directions.keys():
            direction = v.Vector2(self.directions[i][0],self.directions[i][1])
            newLocation = self.test_location(map_size, direction, False)
            if newLocation == v.Vector2(0,0):
                pass
            else:
                dir_keys.append(i)
        return dir_keys
    
#       Set the value of the a Variable  #
    def SetLocation(self, newLocation: v.Vector2) -> None:
        self.location = newLocation
    def SetDirection(self, direction:str):
        if direction in self.directions.keys():
            self.direction = v.Vector2(self.directions[direction][0], self.directions[direction][1])
            return True
        else:
            UserWarning("{d} is not a valid direction to move in".format(d=str(direction)))
            return False
    
#       Game related Methods             #
    def Move(self, map_size: v.Vector2) -> v.Vector2:
        newLocation = self.test_location(map_size, self.direction, True)
        if not newLocation == v.Vector2(0,0):
            self.location = newLocation
        return self.location
    
    def TestSurroundings(self, map_size: v.Vector2) -> list[v.Vector2]:
        surroundings: list [v.Vector2] = []
        for d in self.directions.values():
            surroundings.append(self.location + v.Vector2(d[0],d[1]))
        return surroundings
    
    def test_location(self, map_size: v.Vector2, location: v.Vector2 , isLocationDirection = True):
        # as long as the movement wont go outside of the map, move the character. else the character does not move.
        if self.location.x + location.x < map_size.x and self.location.x + location.x > 0:
            if self.location.y + location.y < map_size.y and self.location.y + location.y > 0:
                if not isLocationDirection:
                    self.direction = location    
                return v.Vector2(self.location.x + self.direction.x, self.location.y + self.direction.y)
        return v.Vector2(0,0)
    ## Movement variables ##
    directions = {"up": [-1, 0], "down": [1, 0],"right":[0, 1],"left": [0, -1]}
    
#### HANDLES THE  IFORMATION REGARDING A SPECIFIC STAT OF AN OBJECT ####
class Stat:
    def __init__(self, value: int | float, min_value: int | float = 1 , max_value: int | float = 0):
        self.value = value
        if value > max_value:
            self.max_value = value
        else:
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
            return True
        else:
            self.value = self.min_value
            return False
    def Reset(self):
        self.value = self.max_value

    ## Stat variables ##
    value: int | float
    min_value: int | float
    max_value: int | float


























