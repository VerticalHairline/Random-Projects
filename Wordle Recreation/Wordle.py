import wordleWords

secretWord = ""
guessNumber = 1
win = False
winCondition = 0

def validWord():
    global guessNumber
    charcterCheck = 0
    
    while True:
        if guessNumber == 1:
            guessWord = input()
        else:
            guessWord = input("Next word guess (Guess #" + str(guessNumber) + "/6) " + "\n" + "\n")

        if guessWord in wordleWords.wordList:
            return guessWord
            break
        else:
            print("Please input a vaild 5 letter word in all lowercase charcters")

def checkWord(word):
    baseText = {
            "letter": "0",
            "in word": False,
            "correctSpot": False,
            "text": "TEST"
                }
    usableLetters = [i for i in secretWord]
    guessArray = [baseText for x in range(0,5)]
    
    for index in range(0, len(word)):
        if word[index] in secretWord and word[index] == secretWord[index] and word[index] in usableLetters:
            guessArray[index] = {
                "letter": word[index],
                "in word": True,
                "correctSpot": True,
                "text": "Correct Position"
                }

            usableLetters.remove(word[index])

    for index in range(0, len(word)):
        if word[index] in secretWord and word[index] in usableLetters and guessArray[index] == baseText:
            guessArray[index] = {
                "letter": word[index],
                "in word": True,
                "correctSpot": False,
                "text": "In word"
                }

            usableLetters.remove(word[index])

    for index in range(0, len(word)):
        if guessArray[index] == baseText:
            guessArray[index] = {
                "letter": word[index],
                "in word": False,
                "correctSpot": False,
                "text": "Not in word"
                }

    return guessArray

def wordDisplay():
    global win
    global guessNumber
    global winCondition
    guessWord = validWord()
    guessArray = checkWord(guessWord)

    for letter in guessArray:
        if letter["correctSpot"] == True:
            winCondition +=1

    if winCondition == 5:
        win = True

    if win == False:  
        for letter in guessArray:
            print("..." + letter['letter'] + "..." + letter['text'])
        guessNumber += 1

def play():
    global secretWord
    global guessNumber
    global win
    global winCondition
    
    secretWord = wordleWords.getWord()
    guessNumber = 1
    win = False
    winCondition = 0
    print("""
=======================================||=======================================
                                Wordle Recreation

                       Enter a valid 5-letter word to begin

                             created by Aiden Pickett
=======================================||=======================================
""")


    while win == False and guessNumber <=6:
        wordDisplay()
        winCondition = 0

    end()

def end():
    global win
    global secretWord
    
    if win == True:
        again = input("Congragulations! you successfully found the hidden word in " + str(guessNumber) + " Guesse(s)." + "\n" + "Would you like to play again? (y)" + "\n" + "\n")
        if again == "y":
            play()
        else:
            quit()
    else:
        again = input("\n" + "Oh no! you could not find the word in the alloted amount of guesses. " + "\n" + "The word was " + secretWord + "\n" + "Would you like to play again? (y)" + "\n")
        if again == "y":
            play()
        else:
            quit()

play()
