import random

def playHiLo():
    secret = random.randrange(1, 101);
    print("I picked a number between 1 and 100. Can you guess it?")
    guess = int(input("Your guess: "))
    while guess != secret:
        if guess < secret:
            print("Too low!")
            guess = int(input("Your guess: "))
        else:
            print("Too high!")
            guess = int(input("Your guess: "))
    print("Congratulations! You got it!")

playHiLo()

