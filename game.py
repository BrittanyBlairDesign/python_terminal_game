

import vectors as v
import characters as char
import map as m
import random as r

def Intro():
    print(" Wecome to Dungeon Crawl\n\tStart\n\tRules\n\tExit")
    selection = input("")
    selection = selection.title()
    while not validateResponse(selection, ['Start', 'Rules', 'Exit'], True):
        selection = input("\n\tStart\n\tRules\n\tExit\n")
    
    if selection == "Start":
        if Start() == True:
            return True
        else: 
            return False
    elif selection == "Rules":
        if Rules() == False:
            return False
        else:
            return True
    else:
        print("Thanks for playing!")
        return False

def Start( playerSymbol = ' '):
   
    # make the game map randomly
    height = r.randint(5,20)
    width = r.randint(5,20)
    game_map = m.Map(width, height)

    # generate  at least one item
    items = []
    for i in range(0, r.randint(1,5)):
        value = r.randint(1,3)
        item = char.Item(value, game_map.map_symbols["item"][0])
        items.append(item)
    game_map.placeItems(items)

    # generate at least 1 enemy
    enemies = {}
    for i in range(0,r.randint(1,5)):
        damage = r.randint(1,3)
        enemy = char.Enemy(game_map.map_size, game_map.map_symbols["enemy"][0], damage)
        enemies[i] = enemy
        game_map.placeItems([enemy])
    
   
    # if its a new game then we choose the player symbol, if its a continuing game we use the same symbol.
    if(playerSymbol == ' '):
        response = input("Please choose a keyboard symbol to represent yourself on the map.\n\t")

        while not validateResponse(response[0], ['#', '&', '.', ',', '|', '~', '-', '_'], False):
            response = input("Sorry that symbol is already bein used on the map to represent something. Please choose a different symbol.")
        
        playerSymbol = response[0]
    game_map.map_symbols["player"][0] = playerSymbol

    # make the player
    player = char.Player(game_map.map_size, playerSymbol, len(enemies.values()) + 1)
    game_map.placeItems([player, '#'])

    return PlayGame(player,enemies,game_map)

def Rules(playerSymbol = '@', inGame = False):
    rules = """
    Navigation:
    \t-Type in the direction you want your character '{ps}' to move in.
    \t\t-'up', 'down', 'right', 'left
    Goals:
    \t-Make your way  to the '#' goal on the displayed map.
    \t-Avoid getting running into or hit by '&' enemies, or you'll loose health.
    \t-Don't run out of health or the game will end.
    """
    print(rules.format(ps=playerSymbol))

    if inGame:
        response = response = input("Would you like to 'Continue' or 'Exit'?\n")

        while not(validateResponse(response,['Continue','Exit'])):
            response = input("Please type 'Continue' to continue plying the game or or 'Exit' to quit the game.\n")
        
        if response == "Exit":
            return response
        
    else:
        response = input("Would you like to 'Start' or 'Exit'?\n")

        while not validateResponse(response, ["Start","Exit"]):
            response = input("Please type 'Start' to begin the game or or 'Exit' to quit the game.\n")
    
        if response == "Start":
            return True
        else:
            return False

def validateResponse(response:str, options:list[str], inclue = True):
    if inclue:
        if response in options:
            return True
        else:
            return False
    else:
        if response in options:
            return False
        else:
            return True        

def PlayGame(Player:char.Player, Enemies, Game_Map:m.Map):
    Game_Status = "playing"

    while Game_Status == "playing":
        print(str(Game_Map))
        Player.PrintInfo()

        command = input("").lower()
        while not validateResponse(command, ['up','down', 'right', 'left', 'exit', 'rules']):
            command = input("1. Type a direction to move in\n2. Type 'Rules' to read the rules of the game.\n3. Type 'exit' to stop playing.\n").lower()

        if command in ['up','down','left','right']:
            result = Game_Map.UpdatePlayerLocation(Player, command)
            
            if validateResponse(result, ['win','lose'], False):
                Game_Status = "playing"
            else:
                Game_Status = result
                break
                 
            for e in range(0,len(Enemies.values())):
                result = Game_Map.UpdateEnemyLocation(Enemies[e])
                if validateResponse(result, ['win','lose'], False):
                    Game_Status = "playing"
                else:
                    Game_Status = result
                    break
        elif command =='rules':
            if Rules(playerSymbol=Player.map_symbol, inGame=True) == 'Exit':
                Game_Status = 'Exit'
                break
        else:
            Game_Status = "Exit"
            break
    
    if Game_Status == "win":
        print("Player Wins!!\nYou managed to escape the dungeon!")
    elif Game_Status == 'lose':
        print("Oh no, you lost this round.")
    print("Thanks for playing!")
    return False


Intro()

