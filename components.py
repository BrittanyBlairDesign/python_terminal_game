# File contains components for various classes to use in the game. 
# Components in file :
#     - Movement

#### HANDLES THE LOCATION AND MOVEMENT OF CLASSES THAT ARE COMPOSED WITH IT ####
class Movement:
    def __init__(self):
        pass
    def __repr__(self) -> str:
        pass
    
    def GetLocation(self):
        return self.location


    ## Movement variables ##
    location = Vector2()