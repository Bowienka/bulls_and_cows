"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Helena Vyplelová
email: vyplelhel@seznam.cz
discord: Helena V. /.helenav.
"""

import random

separator = "-" *55 
number_length = 4

print("Hi there!")
print(separator)
print(f"I've generated a random {number_length} digit number for you.\nLet's play a bulls & cows game.")
print(separator)


def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits)
    return "".join(str(digit) for digit in digits[:number_length])

def get_user_guess():
    while True:
        guess = input("Enter a number: ")
        if not guess.isdigit() or len(set(guess)) != number_length: 
            print("Incorrect number. Please try again.")
            continue
        elif len(guess) != number_length or guess[0] == "0":
            print("Incorrect number. Please try again.")
            continue
        else:     
            return guess          

def evaluate_bulls_and_cows(number, guess):
    bulls = 0
    cows = 0
    for i in range(number_length):
        if guess[i] == number[i]:
            bulls += 1
        else:
            if guess[i] in number:
                cows += 1
    return bulls, cows

def play_game():
    number = generate_number()
    guesses = 0
    while True:
        guess = get_user_guess()
        bulls, cows = evaluate_bulls_and_cows(number, guess)
        guesses += 1
        print("Bulls: {} | Cows: {}".format(bulls, cows))
        if bulls == number_length:
            print(separator)
            print("Correct, you've guessed the secret number in {} guesses!".format(guesses))
            if guesses <= 5:
                print("That's awesome!")
            elif guesses > 5 and guesses <= 15:
                print("That's average.")
            else:
                print("That's no so good.")
            break

if __name__ == "__main__":
    play_game()
