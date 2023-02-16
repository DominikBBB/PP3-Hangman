import random

import colorama
from colorama import Fore, Style
from time import sleep

from words import words
from stages import hangman

import os

from pprint import pprint #############



def clear():
    """
    Clear the terminal 
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """
    Welcome message
    """
    print("*" * 70)
    print(Fore.YELLOW + "Welcome to the Hangman Game!\n")
    print(Fore.RED + "Do you know how you want to hang today?\n")
    print(Style.RESET_ALL + "*" * 70)
    # print(Fore.RED + (hangman[-1])+(hangman[-1])+(hangman[-1]))
    print(Fore.RED + "  +---+"+"  +---+"+"  +---+")
    print(Fore.RED + "  |   |"+"  |   |"+"  |   |")
    print(Fore.RED + "  O   |"+"  O   |"+"  O   |")
    print(Fore.RED + " /|\  |"+" /|\  |"+" /|\  |")
    print(Fore.RED + " / \  |"+" / \  |"+" / \  |")
    print(Fore.RED + "      |"+"      |"+"      |")
    print(Fore.GREEN + "========="+"========="+"=========")
    print(Style.RESET_ALL + "*" * 70)
    sleep(2)
    # clear()
    start_menu()


def start_menu():
    """
    Start the game menu    
    """
    print("Choose one of the options to continue:")
    print("1. Play the Game")
    print("2. Read Instructions/Rules")
    print("3. Quit")
    print("*" * 70)
    start_input = input("Enter your option here:\n")

    if start_input == "1":
        create_user()

    elif start_input == "2":
        rules()
        
    elif start_input == "3":
        quit()

    else:
        clear()
        print(f"You entered: {start_input}. Please enter 1 or 2 or 3.\n")
        sleep(2)
        # start_input = input("Enter your option here:\n")
        # clear()
        # start_game()
        start_menu()


def create_user():
    """
    Takes the player name
    """
    clear()
    print("Your gallows is building up...\n")
    sleep(1)
    print("You will enjoy it!\n")
    sleep(1)
    print("In the meantime...")
    while True:
        user_name = input("Tell me your name (use letters only):\n")
        print("")
        if not user_name.isalpha():
            print("Please enter letters only!\n")
            continue
        else:
            print(Fore.RED + f"Hello {user_name}! Welcome to the game and Good luck!\n")
            sleep(1)
            break
            clear()
    game()


# def get_secret_word():
#     """
#     Get the new secret word
#     (This function can be extended to allow user type their own word)
#     """
#     global secret_word
#     secret_word = random.choice(words)

#     return secret_word.upper()



def game():
    """
    Start the game
    # """
    # secret_word = list(get_secret_word())
    # display = "_" * len(secret_word)
    # print(display)

    number_mistakes = 0
    letters_quessed = []
    number_mistakes_allowed = len(hangman)
    secret_word = random.choice(words)
    letters_word = list(secret_word)
    wrong_letters = []
    
    print()
    print("The word has {} letters".format(len(letters_word)))

    while number_mistakes < number_mistakes_allowed:
        print()
        print("Wrong letters: ", end="")
        for letter in wrong_letters:
            print("{}, ".format(letter), end="")
        print()
        print("Guesses left: {}".format(number_mistakes_allowed - number_mistakes))
        letter_user = input("Enter your letter: ")

                    # isalpha


        while letter_user in letters_quessed or letter_user in wrong_letters:
            print()
            print("You have already entered this letter. Please choose another one!")
            letter_user = input("Enter your new letter: ")

        if letter_user not in letters_word:
            number_mistakes += 1
            wrong_letters.append(letter_user)

        print()
        print("Word: ", end="")

        for letter in letters_word:
            if letter_user == letter:
                letters_quessed.append(letter_user)

        for letter in letters_word:
            if letter in letters_quessed:
                print(letter + " ", end="")
            else:
                print("_ ", end="")

        print()
        if number_mistakes:
            print(hangman[number_mistakes - 1])
        print()
        print("----------------------------")

        if len(letters_quessed) == len(letters_word):
            print()
            print("You won!!!!")
            break

    if number_mistakes == number_mistakes_allowed:
        print()
        print("You lost!")







    
game()









def rules():
    """
    Shows instructions / rules of the game
    """
    clear()
    print(Fore.YELLOW + "*" * 70)
    print(Fore.YELLOW + "Game Golden Rules:\n")

    print(Style.RESET_ALL +
        "A. You will be guessing the secret word by entering single letter at a time.\n"+
        "B. After each incorrectly answered letter your Hangman will start to build.\n"+
        "C. You have 7 lifes. When you loose all, You will be hang!\n"+
        "D. If you love dying. You can start the game again!\n")
    print(Fore.YELLOW + "*" * 70)
    print(Style.RESET_ALL + "Choose one of the options to continue:")
    print("1. Play the Game")
    print("3. Quit")
    print("*" * 70)
    continue_input = input("Enter your option here:\n")

    if continue_input == "1":
        create_user()
    elif continue_input == "3":
        quit()
    else:
        # clear()
        print(f"You entered: {continue_input}. Please enter 1 or 3.")
        sleep(2)
        # continue_input = input("Enter your option here:\n")
        # clear()
        rules()


def quit():
    """
    Goodbye user and end program and start game again
    """
    clear()
    print("*" * 70)
    print("You chose to live longer. Make sure that you enjoy it!\n")
    print("GoodBye and Good luck!\n")
    print("*" * 70)
    sleep(5)
    clear()
    welcome()



# welcome()
