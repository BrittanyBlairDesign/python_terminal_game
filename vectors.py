# Script for Vector classes and vector functions.
# Current Vector classes
#   - Vector2()

# Type alias for Vector2 class
type Vector2  = Vector2

# Operator overloads for Vector2 class
#   Adding 2 vectors    #
def __add__(vector1: Vector2, vector2: Vector2 ):
    return Vector2(vector1.x + vector2.x, vector1.y + vector2.y )

#   Adding a float or int to a vector    #
def __add__(vector1: Vector2, x: float|int):
    return Vector2(vector1.x + x , vector1.y + x)

#   Subtracting 2 vectors   #
def __sub__(vector1: Vector2, vector2: Vector2 ):
    return Vector2(vector1.x - vector2.x, vector1.y - vector2.y)

#   Subtracting a float or int from a vector    #
def __sub__(vector1: Vector2, x: float|int):
    return Vector2(vector1.x - x , vector1.y - x)

#   Setting one vector equal to another   #
def __eq__(vector1: Vector2, vector2: Vector2):
    vector1.x = vector2.x
    vector1.y = vector2.y
    return vector1

### CLASS FOR VECTORS WITH 2 VALUES ###
class Vector2:
    def __init__(self) -> None:
        pass
    def __init__(self, x: float| int):
        self.x = x
        self.y = x
    def __init__(self, x: float| int, y: float | int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        pass

    ## Vector2 Variables ##
    x: float| int = 0
    y: float| int = 0