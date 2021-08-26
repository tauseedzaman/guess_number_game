# A simple guess number game give a try
# Auther: tauseed zaman
import random

def Guess(i):
    random_number = random.randint(1,i)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {i}: "))
        if guess < random_number:
            print("Sorry! Guess again, Too Low")
        elif guess > random_number:
            print("Sorry! Guess again, Too High")
    print(f"\nWow! Congrates, You have Guessed the number {random_number}")



def Computer_Guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low

        feedback = input(f" Is {guess} Too high [H] , Too Low [L] , or Correctly [C]")

        if feedback == "c":
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f" \nYay! The Computer Guessed Your Number {guess} Correctly! ")


#game loop
while True:
    x = input("\nWelcome to Guessing Game\n \
    [1]: You will guess a number and computer will find at\n \
    [2]: Computer will guess a number and you will find at\n")
    rng = int(input("\nEnter higher range of value: "))
    if(x == '1'):
        Computer_Guess(rng)
    else:
        Guess(rng)
    t = input("To play again [Y]/[N]:")
    if t == "n":
        exit()
