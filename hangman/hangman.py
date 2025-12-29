# hangman has 2 legs, 2 arms, 1 body line, 1 head = 6 incorrect guesses.
# need all of the letters in the alphabet.

import string
import random
import re

def get_random_word():
    with open("words.txt", "r") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        random_word = random_line.strip()
        return random_word


# Usage example
random_word = get_random_word().upper()
print(re.sub(r"\S", "-", random_word))

alphabet_list = list(string.ascii_uppercase)
gameOver = False
lettersguessed = ""
inputs = ""
count = 0
graphic = ""
result = ""

# >-|o

def prompt():
    global inputs
    global lettersguessed
    global gameOver
    global count
    global graphic
    global result

    print("Enter your letter:")
    x = input().upper()
    if x in inputs:
        print("Letter already guessed!")
        return
    alphabet_list.remove(x)
    inputs += str(x)
    if x in random_word:
        lettersguessed += str(x)
        result = ""
        for letter in random_word:
            if letter in lettersguessed:
                result += letter
            else:
                result += "-"

        if "-" not in result:
            gameOver = True
            print("You won!")
    else:
        count += 1
    print(inputs )
    print(result)
    match count:
        case 1:
            graphic = """
              +---+
              |   |
                  |
              |   |
                  |
                  |"""
        case 2:
            graphic = """
              +---+
              |   |
                  |
              |   |
             /    |
                  |"""
        case 3:
            graphic = """
              +---+
              |   |
                  |
              |   |
             / \\  |
                  |"""
        case 4:
            graphic = """
              +---+
              |   |
                  |
             /|   |
             / \\  |
                  |"""
        case 5:
            graphic = """
              +---+
              |   |
                  |
             /|\\  |
             / \\  |
                  |"""
        case 6:
            graphic = """
              +---+
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            farewell hangman x_x"""
    print(graphic)


while not (gameOver):
    prompt()
    if count == 6:
        gameOver = True
        print("The word was: " + random_word)
