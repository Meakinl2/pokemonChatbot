def checkInput(availableWords,user_input):
    userWords = user_input.split(" ")
    usedWords = []
    
    for word in userWords:
        
        if word.lower() in availableWords:
            usedWords.append(word)
    
    if usedWords == []:
        
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