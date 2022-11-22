import os,random,pickle,math

from ProjectDataCleaning.fileControl import *

from class_Player import Player
from class_Trainer import Trainer
from class_Battle import Battle




pickle_file_path = selectFile(["SavedObjects","PlayerInstances"],"YEBBV0IIZ2")
with open(pickle_file_path, "rb") as pickle_file:
    pickle_info = pickle_file.read()
    pickle_file.close()
    
player = pickle.loads(pickle_info)

trainer = Trainer(player)


pokemon = player.party[0]

#spliting the users input & check is the inputed word is one of the keywords
def checkInput(availableWords,user_input):
    userWords = user_input.split(" ")
    usedWords = []

 #checks the letters of each word from the users input to see if they match 
    for uWord in userWords:

        for aWord in availableWords:
            accuracy = 0

    for uWord in userWords:
    
        for aWord in availableWords:
            accuracy = 0

            for i in range(0,len(uWord) - 1):

                try:
                    if uWord[i] == aWord[i - 1]:
                        accuracy += 1
                except IndexError:
                    pass

                try:
                    if uWord[i] == aWord[i]:
                        accuracy += 1
                except IndexError:
                    pass

                try:
                    if uWord[i] == aWord[i + 1]:
                        accuracy += 1
                except IndexError:
                    pass

            if len(aWord) - accuracy <= 3:
                usedWords.append(aWord)
    
    return usedWords

        
#iprovment of input matcher and prompt for clarifcation & unecessary info
def battleInput(player,opponent,playerActive,opponentActive,pokemon):
    turn_action = ["Player",player.party.index(pokemon)]
#geting all the posibilety of list for moves, item, op pokemon, and player pokemon
    available_move = []
    for i in range(len(pokemon.knownMoves)):
        available_move.append(pokemon.knownMoves[i].name)

    opponent_pokemon = []
    for i in (opponentActive):
        opponent_pokemon.append(opponent.party[i].nickname)

    available_items = []
    for entry in player.inventory:
        available_items.append(entry)

    player_pokemon = []
    for i in range(len(playerActive.party)):
        player_pokemon.append(player.party[i].nickname)

# turning the player pokemon, move, items, and oppoent pokemon back into indexs
    for i in range(player.party):
        if player.party[i].nickname:
            pass


    opptions = ["swich","check","flee"]


    has_move = False
    has_item = False
    p_pokemon = False
    op_pokemon = False

    print("op" + str(opponent_pokemon))
    print("player" + str(player_pokemon))
    print("item" + str(available_items))
    print("move" + str(available_move))
    
# list of paryts moves, pokemon, and opponent pokemon 
    while True:
        users_input = input("> ")

        if not (has_item and has_move and p_pokemon and op_pokemon):

            playerPokemon = checkInput(player_pokemon,users_input)
            item = checkInput(available_items,users_input)
            move = checkInput(available_move,users_input)
            target_pokemon = checkInput(opponent_pokemon,users_input)

        if len(playerPokemon) == 1:
            p_pokemon = True
        
        if len(target_pokemon) == 1:
            op_pokemon = True

        if len(item) == 1:
            has_item = True
        
        if len(move) == 1:
            has_move = True

        #battle = [op_pokemon and has_move [playerPokemon and move and target_pokemon]]
        #invotory = [has_item and p_pokemon [item and playerPokemon]]
        #move_prompt = [op_pokemon [print("what move would you like to use?")]]
        #error_prompt = [p_pokemon and has_move[print("error try again")],p_pokemon and op_pokemon[print("error try again")],op_pokemon and has_item[print("error try again")],has_item and has_move[print("error try again")]]
        
        if op_pokemon and has_move:
            playerPokemon and move and target_pokemon
        elif has_item and p_pokemon:
            item and playerPokemon 
        elif op_pokemon:
            print("what move would you like to use?")
        elif p_pokemon and op_pokemon:
            print("error try again")
        elif p_pokemon and has_move:
            print("error try again")
        elif op_pokemon and has_item:
            print("error try again")
        elif has_item and has_move:
             print("error try again")
        
        break


print("player " + player.party.index(pokemon))
    
battleInput(player,trainer,[0],[0],pokemon)
