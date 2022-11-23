# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

from ProjectDataCleaning.fileControl import *
import os,random,pickle
from class_Player import Player
from class_Trainer import Trainer
from class_Battle import Battle

def autocorrect(available_words,user_input):
    user_input = user_input.split(" ")
    used_words_lower = []
    checked_positions = []

    # Makes all available words lowercase
    available_words_lower = []
    for word in available_words:
        available_words_lower.append(word.lower())

    # Removing punctuation and checking for exact matches
    for index in range(len(user_input)):
        user_input[index] = user_input[index].strip(r".,;:?!()[]{}''")
        if user_input[index].lower() in available_words_lower:
            print(" ")
            used_words_lower.append(user_input[index])
            checked_positions.append(index)


    # Testing similar length words for basic spelling errors
    for index in (x for x in range(len(user_input)) if x not in checked_positions):
        
        test_word = user_input[index]
        for target_word in available_words_lower:
            
            # If word length too different, following checks are skipped
            if not (-3 < (len(test_word) - len(target_word)) < 3):
                break

            i,j = 0,0
            max_i = len(target_word) - 1
            max_j = len(test_word) - 1
            mistakes = 0
            matches = 0

            test_word_pad = test_word + " " * 3
            target_word_pad = target_word + " " * 3

            if len(target_word) < len(test_word):
                target_word_pad = target_word + " " * (len(test_word) - len(target_word) + 3)

            elif len(test_word) < len(target_word):
                test_word_pad = test_word + " " * (len(target_word) - len(test_word) + 3)


            while i <= max_i and j <= max_j:

                print(f"Checking {target_word_pad[i]} against {test_word_pad[j]}.")
                
                # Check if postions match
                if target_word_pad[i] == test_word_pad[j]:
                    matches += 1
                    mistakes -= 1

                # Checking for subtitution of letters
                elif target_word_pad[i + 1] == test_word_pad[j + 1]:
                    print(f"Checking {target_word_pad[i + 1]} against {test_word_pad[j + 1]}.")
                    print("Substitution 1")
                
                elif target_word_pad[i + 2] == test_word_pad[j + 2]:
                    print(f"Checking {target_word_pad[i + 2]} against {test_word_pad[j + 2]}.")
                    print("Substitution 2")
                    i,j = i + 1,j + 1

                # Checking for insertion of letters
                elif target_word_pad[i] == test_word_pad[j + 1]:
                    print(f"Checking {target_word_pad[i]} against {test_word_pad[j + 1]}.")
                    print("Insertion 1")
                    j += 1

                elif target_word_pad[i] == test_word_pad[j + 2]:
                    print(f"Checking {target_word_pad[i]} against {test_word_pad[j + 2]}.")
                    print("Insertion 2")
                    j += 2

                # Checking for deletion of letters
                elif target_word_pad[i + 1] == test_word_pad[j]:
                    print(f"Checking {target_word_pad[i + 1]} against {test_word_pad[j]}.")
                    print("Deletion 1")
                    i += 1

                elif target_word_pad[i + 2] == test_word_pad[j]:
                    print(f"Checking {target_word_pad[i + 2]} against {test_word_pad[j]}.")
                    print("Deletion 2")
                    i += 2

                else:
                    print("Not close Enough")
                    mistakes += 10
                    break


                mistakes += 1
                print(f"Matches: {matches}")
                print(f"Mistakes: {mistakes}\n")

                i,j = i + 1,j + 1

            if mistakes <= len(target_word) // 3:
                print(f"{test_word} very close match to {target_word}\n")
                used_words_lower.append(target_word)
            else:
                print(f"{test_word} not a very close match to {target_word}\n")

    used_words = []
    for word in used_words_lower:
        index = available_words_lower.index(word)
        used_words.append(available_words[index])

    return used_words


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

            if len(aWord) - accuracy <= 2:
                usedWords.append(aWord)
    
    print(usedWords)
    return usedWords

test_list = [1,2,3]
test_dict = {test_list: "True"}

print(test_dict[[1,2,3]])




exit()

def empty():

    while False:
        try:
            print(f"Current Player Pokemon: {str(target_player_pokemon)}")
            print(f"Current Opponent Pokemon: {str(target_opponent_pokemon)}")
            print(f"Current Item: {str(selected_item)}")
            print(f"Current Move: {str(selected_move)}")
            print(f"Current Option: {str(selected_option)}")
        except UnboundLocalError:
            pass
        
        users_input = input("> ")

        if users_input == "Clear":
            target_player_pokemon = []
            target_opponent_pokemon = []
            selected_item = []
            selected_move = []
            selected_option = []

        temp_list = autocorrect(player_pokemon,users_input)  
        target_player_pokemon = temp_list if len(temp_list) == 1 else target_player_pokemon 

        temp_list = autocorrect(opponent_pokemon,users_input)
        target_opponent_pokemon = temp_list if len(temp_list) == 1 else target_opponent_pokemon

        temp_list = autocorrect(available_items,users_input)
        selected_item = temp_list if len(temp_list) == 1 else selected_item

        temp_list =  autocorrect(available_move,users_input)
        selected_move = temp_list if len(temp_list) == 1 else selected_move

        temp_list = autocorrect(options,users_input)
        selected_option = temp_list if len(temp_list) == 1 else selected_option

        has_player_pokemon = tooManyInputs(target_player_pokemon,"Player Pokemon")  
        has_opponent_pokemon = tooManyInputs(target_opponent_pokemon,"Opponent Pokemon")    
        has_item = tooManyInputs(selected_item,"Player Item")
        has_move = tooManyInputs(selected_move,"Pokemon Move")
        has_option = tooManyInputs(selected_option,"Other Option")
        
        
        if has_player_pokemon and has_item and not [has_move,has_opponent_pokemon,has_option]:
            break

        elif has_opponent_pokemon and has_move and not [has_item,has_player_pokemon,has_option]:
            break

        elif selected_option == ["Check"] and has_player_pokemon and not has_opponent_pokemon:
            index = player_pokemon.index(target_player_pokemon[0])
            player.party[index].printStats

        elif selected_option == ["Check"] and has_opponent_pokemon and not has_player_pokemon:
            index = opponent_pokemon.index(target_opponent_pokemon[0])
            opponent.party[index].printStats
                
        elif selected_option == ["Check"] and not (has_player_pokemon or has_opponent_pokemon):
            print("To use check you need to specify a target pokemon.")

        else:
            print("Too many or not enough inputs.")


