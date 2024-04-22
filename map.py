# Contains a map class that manages what the game board looks like.
import vectors as v
import random as r
import characters as char


class Map:
    def __init__(self, width:int, height:int):
        self.map_size  =  v.Vector2(width,height)
        self.create_map()

    def __repr__(self):
        out_map = ''
        for y in self.map:
            for x in y:
                out_map += str(x)
            out_map += '\n'
        return out_map

    def create_map(self):
        for y in range(0, self.map_size.x + 1):
            row = []
            for x in range(0, self.map_size.y + 1):
                symbol = ' '
                if y == 0 or y == self.map_size.x:
                    symbol = self.map_symbols["wall"][-1]
                elif x == 0 or x == self.map_size.y:
                    symbol = self.map_symbols["wall"][0]
                else:
                    symbol = r.choice(self.map_symbols["floor"])
                row.append(symbol)
            
            self.map.append(row)

    def GetLocationSymbol(self, location:v.Vector2):
        return str(self.map[location.x][location.y])
    
    def GetLocationType(self, symbol:str = '^', location:v.Vector2 = v.Vector2(0,0)):
        if location == v.Vector2(0,0):
            if symbol in self.map_symbols["floor"]:
              return "floor"
            elif symbol in self.map_symbols["wall"]:
                return "wall"
            elif symbol in self.map_symbols["enemy"]:
                return "enemy"
            elif symbol in self.map_symbols["item"]:
                return "item"
            elif symbol in self.map_symbols["player"]:
             return "player"
            elif symbol in self.map_symbols["goal"]:
                return "goal"
        if symbol == '^':
            if self.map[location.x][location.y] in self.map_symbols["floor"]:
                return "floor"
            elif self.map[location.x][location.y] in self.map_symbols["wall"]:
                return "wall"
            elif self.map[location.x][location.y] in self.map_symbols["enemy"]:
                return "enemy"
            elif self.map[location.x][location.y] in self.map_symbols["item"]:
                return "item"
            elif self.map[location.x][location.y] in self.map_symbols["player"]:
                return "player"
            elif self.map[location.x][location.y] in self.map_symbols['goal']:
                return "goal"
        else:
            return "none"
   
    def UpdatePlayerLocation(self, player: char.Player, command:str = 'none'):

        if not command == 'none':

            old_location = player.movement.GetLocation()

            if command in player.movement.directions.keys():
                new_location = player.movement.test_location(self.map_size, v.Vector2(player.movement.directions[command][0], player.movement.directions[command][1]), False)
                locationType = self.GetLocationType(self.GetLocationSymbol(new_location))
                if locationType == "enemy":
                    ## TAKE DAMAGE DO NOT MOVE. ##
                    if isinstance(self.map[new_location.x][new_location.y], char.Enemy):
                        enemy:char.Enemy = self.map[new_location.x][new_location.y]
                        if not player.TakeDamage(enemy.damage.GetValue()):
                            return "lose"
                elif locationType == "item":
                    if command in player.MoveOptions():
                        if isinstance(self.map[new_location.x][new_location.y], char.Item):
                            item:char.Item = self.map[new_location.x][new_location.y]
                            player.Heal(item.GetValue())
                        player.Move(command)
                        print(player.map_symbol)
                        self.map[new_location.x][new_location.y] = player
                        self.map[old_location.x][old_location.y] = r.choice(self.map_symbols["floor"])
                elif locationType == "goal":
                    ## MOVE AND WIN GAME
                    if command in player.MoveOptions():
                        player.Move(command)
                        self.map[new_location.x][new_location.y] = player
                        self.map[old_location.x][old_location.y] = r.choice(self.map_symbols["floor"])
                        return "win"
                elif locationType == "floor":
                    if command in player.MoveOptions():
                        player.Move(command)
                        self.map[new_location.x][new_location.y] = player
                        self.map[old_location.x][old_location.y] = r.choice(self.map_symbols["floor"])
    
    def UpdateEnemyLocation(self, enemy:char.Enemy):

        old_location = enemy.movement.GetLocation()
        RandOption = r.choice(enemy.MoveOptions())

        option = v.Vector2(enemy.movement.directions[RandOption][0], enemy.movement.directions[RandOption][1])
        new_location = enemy.movement.test_location(self.map_size, option, False)
        locationType = self.GetLocationType(self.GetLocationSymbol(new_location))
        if locationType == "player":
            ## DAMAGE PLAYER DO NOT MOVE
            if isinstance(self.map[new_location.x][new_location.y], char.Player):
                player:char.Player = self.map[new_location.x][new_location.y]
                if not player.TakeDamage(enemy.damage.GetValue()):
                    return "lose"
        elif locationType == "floor":
            enemy.Move(RandOption)
            self.map[new_location.x][new_location.y] = enemy
            self.map[old_location.x][old_location.y] = self.map_symbols["floor"][r.choice([0,1])]
            
    def placeItems(self, items:list):
        for i in items:
            placed = False
            while not placed:
                width = r.randint(1, self.map_size.x)
                height = r.randint(1,self.map_size.y)
                currentsymbol= self.GetLocationSymbol(location=v.Vector2(width,height))
                if currentsymbol in self.map_symbols["floor"]:
                    if isinstance(i, char.Player):
                        player: char.Player = i
                        player.movement.SetLocation(v.Vector2(width,height))
                        self.map[width][height] = player
                        placed = True
                    elif isinstance(i, char.Enemy):
                        enemy: char.Enemy = i
                        enemy.movement.SetLocation(v.Vector2(width,height))
                        self.map[width][height] = enemy
                        placed = True
                    else:
                        self.map[width][height] = i
                        placed = True
       
    ## map variables ##
    map_size: v.Vector2 = v.Vector2(3,3)
    map = []
    map_symbols = {"wall": ['|', '-'], 
                                         "floor": ['.', ' '], 
                                         "enemy":['&'], 
                                         "item": ['*'], 
                                         "player": ['@'], 
                                         "goal":["#"]}
