# A file to control all the things that require user input, so it's easier to see what the chatbot will need to know.
# Will probably see massive changes when the chatbot is properly implemented

from dictonaries import *

# ---------------------------------------------------------------------------------

# Re-Occuring functions, need to be well refined

# For checking user answer when required yes or no
# Could be expanded quite easily with a dictionary for positive and negative confiramtions
def yes_or_no():
    
    while True:
        user_input = input(" > ")
        
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Not a valid affirmation nor negation. Please try again. ")

# ---------------------------------------------------------------------------------

# Inital setup functions, only runs once, doesn't need too much interpretation

# Ask what name the player would like to use
def pickPlayerName(player):
    namePicked = False
    
    while not namePicked:
        print("What name would you like to use?")
        user_input = input(" > ")
        print(f"You would like to be known as {user_input}. Is that correct? ")
        
        if yes_or_no():
            player.name = user_input
            namePicked = True
        else:
            print(f"I suppose you should give it another try then.")
    print(f"Hello {player.name}. It's nice to meet you.")


# Asking what starting pokemon the player would like to use
def pickStartingPokemon(player):
    print(f"""To begin your adventure you are going to require a Pokémon. You may choose from of these three: 
Bulbasaur the Grass type, Charmander the Fire type or Squirtle the Water type.
They might not look very powerful now, but given some time, a bit of practice and plently of love,
I assure you they will grow to be among the powerful Pokémon to ever live. """)
    print(f"So {player.name}, who will it be?")
    user_input = input(" > ")
    starter  = user_input
    validInput = False
    
    while not validInput:
        
        if starter.lower() in ["bulbasaur","charmander","squirtle"]:
            print(f"You would like to take care of {starter}?")
            
            if yes_or_no():
                f"{starter} looks gleefully at you. This might just be the start of a beautiful freindship."
                validInput = True 
            else:
                print(f"I'm sure {starter} will find a trainer in no time, but who to pick instead?")
                starter = input(" > ")
        else:
            print(f"I'm sorry {player.name}, but I'm not sure what you mean. Could you repeat that?")
            starter = input(" > ")
    
    print(f"Would you like to give {starter} a nickname?")
    nickname = starter[0].upper() + starter[1:len(starter)].lower()
    
    if yes_or_no():
        print(f"What would you like {starter} to be known as?")
        user_input = input(" > ")
        nickname = user_input
        assignedName = False
        
        while not assignedName:
            print(f"{nickname}, is that correct? ")
            
            if yes_or_no(): 
                assignedName =  True
            else:
                print("You should probably try again then.")
                nickname = input(" > ")

    return starting_pokemon[starter.lower()], nickname

# ---------------------------------------------------------------------------------

# Battle-related inputs

# Takes input from the user to return a list with information for the  
def userBattleMain(player,opponent,playerPokemon,playerActive,opponentActive):
    validInput = False
    
    while not validInput:
        turnAction = []
        print(" 1. Move \n 2. Item \n 3. Switch \n 4. Flee")
        user_input = input(" > ")

        if user_input.lower() in ["1","move"]:
            turnAction.append("Move")
            moveIndex = userBattleMove(player,playerPokemon)
            turnAction.append(moveIndex)
            pokemonIndex = userBattleSelectPokemon(opponentActive,playerPokemon.knownMoves[moveIndex].name)
            turnAction.append(pokemonIndex)
            print(f"You want to use {playerPokemon.knownMoves[moveIndex].name} against {opponentActive[pokemonIndex].nickname}? ")
            validInput = yes_or_no()

        elif user_input.lower() in ["2","item"]:
            turnAction.append("Item")
            item = userBattleItem(player.inventory)
            
            if item != "":
                turnAction.append(item)
                pokemonIndex = userBattleSelectPokemon(player.party,item)
                turnAction.append(pokemonIndex)
                print(f"You want to use {item} on {player.party[pokemonIndex].nickname}?")
                validInput = yes_or_no()

        elif user_input.lower() in ["3","switch"]:
            turnAction.append("Switch")
            pokemonIndex = userBattleSelectPokemon(player.party,"switch")
            turnAction.append(pokemonIndex)
            print(f"Switch out {playerPokemon.nickname} and switch in {player.party[pokemonIndex].nickname}?")
            validInput = yes_or_no()

        elif user_input.lower() in ["4","flee"]:
            turnAction.append("Flee")
            print("You want to run away? Are you sure?")
            validInput = yes_or_no()

        else:
            print(f"Sorry {player.name}, but I don't know what it is you mean. Could you try again, please?")

    return turnAction


# To pick a move to use from the available moveset
def userBattleMove(player,playerPokemon):
    print(f"{playerPokemon.nickname} has availale, moves: ")
    validInput = False

    while not validInput:
        for i in range(0,len(playerPokemon.knownMoves)):
            print(f" {i + 1}. {playerPokemon.knownMoves[i].name} ")

        print(f"What move should {playerPokemon.nickname} use?")
        user_input = input(" > ")
        
        try:
            if int(user_input) in range(1,len(playerPokemon.knownMoves) + 1):
                moveIndex = int(user_input) - 1
                validInput = True
            else:
                print(f"Sorry {player.name}, but {playerPokemon.name} doesn't have a move with at that index.")

        except ValueError:
            print(f"Sorry {player.name}, but I don't know what it is you mean. Could you try again, please?")

        return moveIndex
        

# To pick and use an item in battle
def userBattleItem(Inventory):
    
    if Inventory == {}:
        print("Sorry, you're inventory appears to be empty")
        return ""
    
    validInput = False
    
    while not validInput:
        print("Available Items:")
        
        for item in Inventory:
            print(f" - {item}: {Inventory[item]}")
        print("Which item would you like to use? ")
        user_input = input(" > ")
        
        if user_input[0].upper() + user_input[1:-1].lower() in Inventory:
            item = user_input
            validInput = True
        
        else:
            print(f"Sorry, you don't have any {user_input} to use. Try again?")
    
    return item

        
# To select a pokemon, for either a move, an item or for switching in
def userBattleSelectPokemon(affectablePokemon,action):
    validInput = False

    while not validInput:
        print("Affectable Pokemon: ")
        for i in range(len(affectablePokemon)) :
            print(f" - {i + 1}. {affectablePokemon[i].nickname}")

        if action != "switch":
            print(f"On which pokemon do you want to use {action}? ")
        else:
            print(f"Who should switch in?")
        user_input = input(" > ")

        try:
            if int(user_input) in range(1,len(affectablePokemon) + 1):
                pokemonIndex = int(user_input) - 1
                validInput = True

            else:
                print("There is pokemon at the given index. Please re-enter.")

        except ValueError:
            print(f"Sorry, but I don't know what it is you mean. Could you try again, please?")

    return pokemonIndex

 
# ---------------------------------------------------------------------------------

# Pokemon Events

# Asks user if they want replace an old move, when their pokemon levels up and tries to learn a new move.
def learnLevelMove(pokemon,newMove):
    print(f"{pokemon.nickname} wants to learn {newMove}.")
    print(f"Would you like {pokemon.nickname} to forget an old move and learn {newMove}?")
    
    if yes_or_no():
        print(f"{pokemon.nickname} knows the moves:")
        
        for move in pokemon.knownMoves:
            print(move.name)
        moveChosen = False
        
        while not moveChosen:
            print(f"Which move should {pokemon.nickname} forget?")
            user_input = input(f" > ")
            
            for i in range(len(pokemon.knownMoves)):
                
                if user_input.lower() == pokemon.knownMoves[i].name.lower():
                    print(f"{pokemon.nickname} should forget {user_input}?")
                    
                    if yes_or_no():
                        pokemon.assignNewMove(pokemon.knownMoves[i],newMove)
                        print(f"{pokemon.nickname} has successfully learnt {newMove}.")
                        moveChosen = True

            if user_input == "cancel":
                print(f"{pokemon.nickname} did not learn {newMove}.")
                break

    else:
        print(f"{pokemon.nickname} did not learn {newMove}.")