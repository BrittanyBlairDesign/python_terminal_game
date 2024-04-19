# Script for Vector classes and vector functions.
# Current Vector classes
#   - Vector2()

# Type alias for Vector2 class
type Vector2  = Vector2

### CLASS FOR VECTORS WITH 2 VALUES ###
class Vector2:
    def __init__(self, x: float| int = 0, y: float | int = 0) -> None:
        self.x = x
        self.y = y

    # Operator overloads for Vector2 class  #
    #   Adding 2 vectors    #
    def __add__(self, vector2: Vector2 ) -> Vector2:
        return Vector2(self.x + vector2.x, self.y + vector2.y )

    #   Adding a float or int to a vector    #
    def __add__(self, x: float|int) -> Vector2:
        return Vector2(self.x + x , self.y + x)

    #   Subtracting 2 vectors   #
    def __sub__(self, vector2: Vector2 ) -> Vector2:
        return Vector2(self.x - vector2.x, self.y - vector2.y)

    #   Subtracting a float or int from a vector    #
    def __sub__(self, x: float|int) -> Vector2:
        return Vector2(self.x - x , self.y - x)

    #   Setting one vector equal to another   #
    def __eq__(self, vector2: Vector2) -> Vector2:
        self.x = vector2.x
        self.y = vector2.y
        return self

    #   Setting one vector to += another    #
    def __iadd__(self, vector2: Vector2) -> Vector2:
        self.x += vector2.x
        self.y += vector2.y
        return self
    
    #   Prints out (x,y) when printing a vector #
    def __repr__(self) -> str:
        return "({x},{y})".format(x=str(x),y=str(y))

    ## Vector2 Variables ##
    x: float| int = 0
    y: float| int = 0