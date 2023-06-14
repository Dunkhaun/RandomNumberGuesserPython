import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it within 10 attempts?")

    while attempts < max_attempts:
        attempts += 1
        guess = get_valid_input()

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")

    if attempts >= max_attempts:
        print(f"Game over! The number was {number}.")
        play_again()

def get_valid_input():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            else:
                return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes":
            play_game()
            break
        elif choice.lower() == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

play_game()
