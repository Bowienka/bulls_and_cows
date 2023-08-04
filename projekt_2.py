"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Helena Vyplelová
email: vyplelhel@seznam.cz
discord: Helena V. /.helenav.
"""

import random

separator = "-" *55 

print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.\nLet's play a bulls & cows game.")
print(separator)


def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(str(digit) for digit in digits[:4])

def get_user_guess():
    while True:
        guess = input("Enter a number: ")
        if not guess.isdigit() or len(set(guess)) != 4: 
            print("Incorrect number. Please try again.")
            continue
        elif len(guess) != 4 or guess[0] == "0":
            print("Incorrect number. Please try again.")
            continue
        else:     
            return guess          

def evaluate_bulls_and_cows(number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
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
        if bulls == 4:
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