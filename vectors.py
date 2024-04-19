# Script for Vector classes and vector functions.
# Current Vector classes
#   - Vector2()

type Vector2 = Vector2
def __add__(Vector2_1: Vector2, Vector2_2: Vector2 ):
    pass

### CLASS FOR VECTORS WITH 2 VALUES ###
class Vector2:
    def __init__(self) -> None:
        pass
    def __init__(self, x):
        self.x = x
        self.y = x
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        pass

    ## Vector2 Variables ##
    x = 0
    y = 0