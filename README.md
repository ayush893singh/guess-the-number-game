# guess-the-number-game
This is a simple Python number guessing game. The program generates a random number between 1 and 100 and asks the user to guess it. Hints like "Guess Higher" or "Guess Lower" are given until the correct answer is guessed.

import  random
jackpot = random.randint(1,100)
guess = int(input("Guess the Number : "))
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else : 
        print("Guess lower")
    guess = int(input("Guess the Number : "))
print("-----Sahi jawab-----")
