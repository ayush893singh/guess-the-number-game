import random
jackpot = random.randint(1, 100)
guess = int(input("Guess the Number : "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess lower")
    
    guess = int(input("Guess the Number : "))
    counter += 1

print("--------Sahi jawab--------")
print("you took", counter, "attempts")