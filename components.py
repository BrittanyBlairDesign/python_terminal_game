# File contains components for various classes to use in the game. 
# Components in file :
#     - Movement

import vectors

#### HANDLES THE LOCATION AND MOVEMENT OF CLASSES THAT ARE COMPOSED WITH IT ####
class Movement:
    def __init__(self):
        pass
    def __repr__(self) -> str:
        pass

#       Return the value of a variable   #
    def GetLocation(self) -> vectors.Vector2:
        return self.location
    def GetDirection(self) -> vectors.Vector2:
        return self.direction
    def GetPossibleDirections(self) -> str[str]:
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
    
#       Game related Methods             #
    def Move(self) -> vectors.Vector2:
        pass
    def isMoveValid(self):
        pass
    
    ## Movement variables ##
    location: vectors.Vector2 = vectors.Vector2()
    direction: vectors.Vector2 = vectors.Vector2(0)
    directions = {"up":   [-1, 0],
                  "down": [1, 0],
                  "right":[0, -1],
                  "left": [0, 1]}