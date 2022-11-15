#creating a function to check for key words in input (Autocorrector)
users_party = {
    "B":["Takckle", "overgrown", "Harden"],
    "Charmander":["Quick attack", "Fire Punch", "Tail whip"],
    "Squrtal":["ice punch", "water gun", "tail whip"]
}
 
oppnent_party = {
    "Growlithe": ["Ember", "Flamethrower", "Roar"],
    "machomp": ["Take Down", "Gust", "Combat Punch"]
}
#------------------------------------------------------------------------------------------------
def battleInput(player,oppent):
    while True:
        users_input = input("> ").split(" ")

        if all(item, move, target_pokemon) == None:


            for word in users_input:
                item = checkInput
                move = checkInput

                target_pokemon = checkInput


#spliting the users input & check is the inputed word is one of the keywords
def checkInput(availableWords,user_input):
    userWords = user_input.split(" ")
    usedWords = []

 #checks the letters of each word from the users input to see if they match 
    for uWord in userWords:

        for aWord in availableWords:
            accuracy = 0
            print(f"Checking {uWord} against {aWord}.")

    for uWord in userWords:
    
        for aWord in availableWords:
            accuracy = 0
            print(f"Checking {uWord} against {aWord}.")

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


#see if it maches with the keywords

def cheak_input (avablewords,user_Input):
    user_Words = user_Input.split(" ")
    user_Words = []
    for words in user_Words:
        if words.lower in avablewords:
            user_Words.append(words) 
            cheak_input(words=avablewords)
        

# spliting the user input for words
def input_checker(user_party, oppent_party, user_input):
    user_words = user_input.split(" ")
    
# sees if user input matches with the dictonary for moves
    for word in user_words:

        print ("word: " + word)

        for entry in user_party:
            if word.lower() == entry.lower():
                user_words.append(entry)
                print ("\nselected Attacker: " + move)

            for move in user_party[entry]:
                print("move: " + " ". join(map(str,move)))

                if word.lower() == move.lower:
                    user_words.append(move)
                    print("Slected Move: " + move)


# sees if user input matches with the dictonary for pokemon

            for animal in user_party:
                if word.lower() == animal.lower():
                    user_words.append(animal)
                    print("\nChosen pokemon: " + pokemon)
                
                for pokemon in user_party[pokemon]:
                    print ("pokenon: " + pokemon)

                    if word.lower() == pokemon.lower:
                        user_words.append(pokemon)
                        print("Selected pokmon: " + " ". join(map(str,pokemon)))

# sees if user input matches with the dictonary for oppent pokemon

            for op_pokemon in oppent_party:
                if word.lower() == op_pokemon.lower():
                    user_words.append(op_pokemon)
                    print ("\n oppent pokemon is: " + oppent)

                for oppent in oppent_party[oppent]:
                    print("oppent pokemon: " + oppent)

                    if word.lower() == oppent.lower:
                        user_words.append(oppent)
                        print("Selected oppent pokemon: " + " ". join(map(str,oppent)))
input_checker(users_party,oppnent_party,users_party)

#checking for requirments:

