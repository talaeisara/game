import random

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome to Guess The Number!my cute game")
print("Guess a number between 1 and 100")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # something
        print("You guessed it!")
        print("Attempts:", attempts)
