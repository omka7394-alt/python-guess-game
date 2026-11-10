import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try higher.")
    elif guess > secret_number:
        print("Too high! Try lower.")
    else:
        print(f"Congratulations! You won in {attempts} attempts!")
        break
