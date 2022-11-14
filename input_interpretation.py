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

# sees if user input matches with the dictonary for moves
def pokemon(user_party, oppent_party, user_input):
    user_words = user_input.split(" ")
    
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

# -----------------------------------------------------------------------------------
# sees if user input matches with the dictonary for pokemon
        for pokemon in user_words:
            print ("pokemon is: " + pokemon)

            for Poke_mon in user_party:
                if word.lower() == Poke_mon.lower():
                    user_words.append(Poke_mon)
                    print("\nChosen op_pokemon: " + Poke_mon)
                
                for Poke_mon in user_party[Poke_mon]:
                    print ("pokenon: " + Poke_mon)

                    if word.lower() == pokemon.lower:
                        user_words.append(pokemon)
                        print("Selected pokmon: " + " ". join(map(str,pokemon)))



#spliting the users input & check is the inputed word is one of the keywords
def checkInput(availableWords,user_input):
    userWords = user_input.split(" ")
    usedWords = []

 #checks the letters of each word from the users input to see if they match 
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
        
 