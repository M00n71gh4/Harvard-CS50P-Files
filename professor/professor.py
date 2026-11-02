import random


def main():
    scoreCount = 0
    GameLevel = get_level()

    for i in range(10):
        wrongAnswerCount = 0
        NewTry = True


        a = generate_integer(GameLevel)
        b = generate_integer(GameLevel)
        mathSum = a + b

        while NewTry == True:
            answer = ""

            while answer.isdigit() == False:
                print(f"{a} + {b} =", end=" ")
                answer = input()

                if answer.isdigit() == False:
                    print("EEE")

            answer = int(answer)

            if answer == mathSum:
                NewTry = False
                scoreCount += 1
            else:
                wrongAnswerCount += 1
                #answer = ""
                print("EEE")
            if wrongAnswerCount >= 3:
                NewTry = False
                print(f"{a} + {b} = {mathSum}")

    print(f"Score: {scoreCount}")






def get_level():
    doLoop = True

    while doLoop == True:
        inputLevel = input("Level: ")

        if inputLevel.isdigit() == True:
            inputLevel = int(inputLevel)
            if inputLevel > 0 and inputLevel < 4:
                doLoop = False
                return(inputLevel)


def generate_integer(level):
    randomInt = 0

    match level:
        case 1:
            randomInt = random.randint(0,9)
        case 2:
            randomInt = random.randint(10,99)
        case 3:
            randomInt = random.randint(100,999)
        case _:
            raise ValueError

    return(randomInt)


if __name__ == "__main__":
    main()