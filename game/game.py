import random
gameLevel = False
gameGuess = False
levelInput = ""
gameInput = ""
rnd = 0

def validateInput(userInput):
    try:
        if int(userInput) > 0:
            return(True)
        else:
            return(False)
    except ValueError:
        return(False)


while gameLevel == False:
    levelInput = input("Level: ")
    gameLevel = validateInput(levelInput)

rnd = random.randint(1, int(levelInput))

while gameGuess == False:
    gameInput = input("Guess: ")
    gameGuess = validateInput(gameInput)

    if gameGuess == True:
        gameInput = int(gameInput)

        if gameInput < gameInput:
            print(f"Too large!")

        if rnd == gameInput:
            print("Just right!")
        elif rnd > gameInput:
            print("Too small!")
            gameGuess = False
        else:
            print(f"Too large!")
            gameGuess = False