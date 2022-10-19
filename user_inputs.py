# A file to control all the things that require user input, so it's easier to see what the chatbot will need to know.
# Will probably see massive changes when the chatbot is properly implemented

# For checking user answer when required yes or no
# Could be expanded quite easily with a dictionary for positive and negative confiramtions
def yes_or_no():
    while True:
        user_input = input("> ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False


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

