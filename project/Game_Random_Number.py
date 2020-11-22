import random

randomNumber = random.randint(1,100)

print(randomNumber)
userGuess = None
guesses = 0

while(userGuess != randomNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1

    if(userGuess == randomNumber):
        print(f"You guessed it right in {guesses} guesses")
        break
    
    else:
        if(userGuess > randomNumber):
            print(f"Entered number is greater than the actual number")
        else:
            print(f"Entered number is smaller than the actual number")

with open("highScore.txt") as f:
    val = f.read()

    if(val == "" or int(val) > guesses):
        print("You have the highest score")
        with open("highScore.txt",'w') as f:
            f.write(str(guesses))
    
    else :
        print(f"Your score is {guesses} whereas highest score is {val}")
