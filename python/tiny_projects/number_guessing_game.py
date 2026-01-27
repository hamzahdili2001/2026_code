#!/usr/bin/env python3


import random

# get a random number
random_number = random.randint(1,100)

attempts_count = 0
attempts_limit = 20

print("Welcome to the Guessing Game! Try to guess the number between 1 and 100.")


while attempts_limit > 0:
    user_guess = input(f"Guess a number (You have {attempts_limit} attempts left): ")


    #check user input if its an int
    if user_guess.isdigit():
        guess = int(user_guess)
        attempts_count += 1
        attempts_limit -= 1
        
        if guess > random_number:
            print("too high")

        elif guess < random_number:
            print("too low")

        else:
            print(f"Correct! You guessed it in {attempts_count} attempts. Congratulations! 🎉")
            break
        
    else:
        print("Input is not a number. Try again!")
        
        

# If user runs out of attempts
if attempts_limit == 0 and guess != random_number:
    print(f"Game Over! The number was {random_number}.")
