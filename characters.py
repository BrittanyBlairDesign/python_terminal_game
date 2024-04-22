# file contains character classes for the game. 
# characters in file
#       - Player
#       - Enemy

import components as c
import vectors as v
import random as r

class MovingCharacter:
    def __init__(self, map_size: v.Vector2, map_symbol: str):
        self.map_size = map_size
        self.map_symbol = map_symbol
    def __repr__(self):
        return self.map_symbol

    def Move(self, command:str):
        if self.movement.SetDirection(command):
            newLocation:v.Vector2 = self.movement.Move(self.map_size)
            return newLocation
    def MoveOptions(self):
        return self.movement.GetPossibleDirections(self.map_size)

    ## Variable for moving characters ##
    movement: c.Movement = c.Movement(v.Vector2(0,0))
    map_symbol: str = 'x'
    map_size: v.Vector2 = v.Vector2()

class Enemy(MovingCharacter):
    def __init__(self, map_size: v.Vector2, map_symbol: str, damage:int):
        MovingCharacter.__init__(self, map_size, map_symbol)
        self.damage = c.Stat(damage)

    ## Variables for Enemies
    damage:c.Stat = c.Stat(1)

class Player(MovingCharacter):
    def __init__(self, map_size: v.Vector2, map_symbol:str, health:int = 3):
        MovingCharacter.__init__(self, map_size, map_symbol)
        self.health = c.Stat(health)

    def TakeDamage(self, damage:int):
        alive = self.health.Decrease(damage)
        print("Player got hit by an enemy and takes {d} damage.\nPlayer Health : {h}".format(d=str(damage),h=str(self.health)))
        return alive

    def Heal(self, amount:int):
        self.health.Increase(amount)
        print("Player's health has increased by {a}. Health is now {h}".format(a=amount,h=str(self.health)))


    def PrintInfo(self):
        info = """"
        Player : {symbol}
        \tHealth - {health}
        \tPossible Movements - {moves}
        \tLocation - {location}
        """
        print(info.format(symbol=self.map_symbol, health=str(self.health), moves=str(self.MoveOptions()),location=str(self.movement.location)))


    ## Variable for Player ##
    health:c.Stat = c.Stat(3)

class Item:
    def __init__(self, Value, map_symbol):
        self.value = Value
        self.map_symbol = map_symbol
    def __repr__(self):
        return self.map_symbol

    def GetValue(self):
        return self.value
    ## Variable for Item
    value:int = 0
    map_symbol:str = '*'