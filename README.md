## guess-the-number-game
Guess the Number Game ek simple interactive game hai jisme computer ek random number choose karta hai aur user ko usse guess karna hota hai.
Har galat guess par hints (higher/lower) milte hain, aur sahi answer tak pahunchne ke liye attempts count kiye jaate hain.

## Technologies Used
Python – Core programming language
random module – Used to generate a random number (randint)
Input/Output functions – input() and print() for user interaction

## How It Works
The program generates a random number between 1 and 100.
The user is asked to guess the number.
A loop runs until the correct number is guessed:
If the guess is too low, it prints "Guess Higher".
If the guess is too high, it prints "Guess lower".
Each guess increases the attempt counter.
Once guessed correctly:
It displays a success message.
Shows how many attempts were taken.

## Code
```
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
```
## Output (Example Run)
```
Guess the Number : 50
Guess Higher
Guess the Number : 75
Guess lower
Guess the Number : 65
Guess Higher
Guess the Number : 70
--------Sahi jawab--------
you took 4 attempts
```
## Author
Ayush Singh
https://github.com/ayush893singh
