# A file to control all the things that require user input, so it's easier to see what the chatbot will need to know.
# Will probably see massive changes when the chatbot is properly implemented

from dictonaries import *

# For checking user answer when required yes or no
# Could be expanded quite easily with a dictionary for positive and negative confiramtions
def yes_or_no():
    while True:
        user_input = input("> ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Not a valid affirmation nor negation. Please try again. ")


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
            user_input = input(f"Which move should {pokemon.nickname} forget? \n> ")
            
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


# Ask what name the player would like to use
def pickPlayerName(player):
    namePicked = False
    while not namePicked:
        user_input = input(f"What name would you like to use? \n> ")
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
    starter = input(f"So {player.name}, who will it be? \n> ")
    validInput = False
    while not validInput:
        if starter.lower() in ["bulbasaur","charmander","squirtle"]:
            print(f"You would like to take care of {starter}?")
            if yes_or_no():
                f"{starter} looks gleefully at you. This might just be the start of a beautiful freindship."
                validInput = True 
            else:
                starter = input(f"I'm sure {starter} will find a trainer in no time, but who to pick instead? \n> ")
        else:
            starter = input(f"I'm sorry {player.name}, but I'm not sure what you mean. Could you repeat that? \n> ")
    
    print(f"Would you like to give {starter} a nickname?")
    nickname = starter[0].upper() + starter[1:len(starter)].lower()
    if yes_or_no():
        nickname = input(f"What would you like {starter} to be known as? \n> ")
        assignedName = False
        while not assignedName:
            print(f"{nickname}, is that correct? ")
            if yes_or_no(): 
                assignedName =  True
            else:
                nickname = input("You should probably try again then. \n> ")

    return starting_pokemon[starter], nickname
