def checkInput(availableWords,user_input):
    userWords = user_input.split(" ")
    usedWords = []

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


def cheak_input (avablewords,user_Input):
    user_Words = user_Input.split(" ")
    user_Words = []
    for words in user_Words:
        if words.lower in avablewords:
            user_Words.append(words)


    if user_Words ==[]:
        for uWords in avablewords:
            found_match = False 

            for aWords in range(1,len(uWords)-1):
                acuarcy =0
                print(uWords)

            if not found_match:

                for i in range(0,len(uWords)-1):

                    try:
                        if uWords[i]==aWords[i]:
                            accuracy+=1
                    except IndexError:
                        pass

                    try:
                        if uWords[i] ==aWords[i]:
                            accuracy+=1
                    except IndexError:
                        pass 

                    try: 
                        if uWords[i]==aWords[i+1]:
                            accuracy+=1
                    except IndexError:
                            pass

                print(f"final accuracy: {accuracy}")
                if len(words) - accuracy <=3:
                    user_Words.append(aWords)
        return(user_Words)  
