import random

import colorama
from colorama import Fore, Style
from time import sleep

from words import words
from stages import hangman

import os


def clear():
    """
    Clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """
    Welcome message
    """
    clear()
    print("*" * 80)
    print(Fore.YELLOW + "Welcome to the Hangman Game!\n")
    print(Fore.RED + "Do you know how you want to hang today?\n")
    print(Style.RESET_ALL + "*" * 80)
    print(Fore.RED + "  +---+"+"  +---+"+"  +---+")
    print(Fore.RED + "  |   |"+"  |   |"+"  |   |")
    print(Fore.RED + "  O   |"+"  O   |"+"  O   |")
    print(Fore.RED + " /|\  |"+" /|\  |"+" /|\  |")
    print(Fore.RED + " / \  |"+" / \  |"+" / \  |")
    print(Fore.RED + "      |"+"      |"+"      |")
    print(Fore.GREEN + "========="+"========="+"=========")
    print(Style.RESET_ALL + "*" * 80)
    sleep(2)
    start_menu()


def start_menu():
    """
    Start the game menu
    """
    print("Choose one of the options to continue:")
    print("1. Play the Game")
    print("2. Read Instructions/Rules")
    print("3. Exit\n")
    start_input = input("Enter your option here:\n")

    if start_input == "1":
        user_name()
    elif start_input == "2":
        rules()
    elif start_input == "3":
        exit()
    else:
        clear()
        print(f"You entered: {start_input}. Please enter 1 or 2 or 3.\n")
        sleep(2)
        start_menu()


def user_name():
    """
    Takes the player name
    """
    clear()
    print("Your gallows is building up...\n")
    sleep(1)
    print("You will enjoy it!\n")
    sleep(1)
    print("In the meantime...\n")
    while True:
        user_name = input("Tell me your name "
                          + "(use letters only):\n").capitalize()
        print()
        if not user_name.isalpha():
            print("Please enter"+Fore.YELLOW
                  + " letters "+Style.RESET_ALL+"only!\n")
            continue
        else:
            clear()
            print("*" * 80)
            print(Fore.RED + f"Hello {user_name}! "
                  + "Welcome to the game and Good luck!\n")
            sleep(1)
            break
    game()


def game():
    """
    Start the game function
    Code based on YT: https://youtu.be/lJ7RhvNvsnc
    """
    number_mistakes = 0
    letters_guessed = []
    number_mistakes_allowed = len(hangman)
    secret_word = random.choice(words).upper()
    letters_word = list(secret_word)
    wrong_letters = []

    print(Style.RESET_ALL + "*" * 80)
    print(Fore.YELLOW + "The word has {} letters".format(len(letters_word)))

    while number_mistakes < number_mistakes_allowed:
        print()
        print(Fore.RED + "Wrong letters: ", end="")
        for letter in wrong_letters:
            print("{}, ".format(letter), end="")
        print()
        print(Style.RESET_ALL+"Guesses left: {}".format(
              number_mistakes_allowed - number_mistakes))
        while True:
            letter_user = input("Enter your letter: \n").upper()
            print()
            if not letter_user.isalpha() and len(letter_user) == 1:
                print("Please enter"+Fore.YELLOW
                      + " single letter "+Style.RESET_ALL+"only!\n")
                continue
            else:
                break

        while letter_user in letters_guessed or letter_user in wrong_letters:
            print()
            print("You have already entered this letter. "
                  + "Please choose another one!\n")
            while True:
                letter_user = input("Enter your new letter: \n").upper()
                print()
                if not letter_user.isalpha() and len(letter_user) == 1:
                    print("Please enter"+Fore.YELLOW
                          + " single letter "+Style.RESET_ALL+"only!\n")
                    continue
                else:
                    break

        if letter_user not in letters_word:
            number_mistakes += 1
            wrong_letters.append(letter_user)
        print()
        print("Word: ", end="")

        for letter in letters_word:
            if letter_user == letter:
                letters_guessed.append(letter_user)

        for letter in letters_word:
            if letter in letters_guessed:
                print(letter + " ", end="")
            else:
                print("_ ", end="")

        print()
        if number_mistakes:
            print(Fore.RED + hangman[number_mistakes - 1])
        print()
        print(Style.RESET_ALL + "*" * 80)

        if len(letters_guessed) == len(letters_word):
            print()
            print(Fore.RED + "Excellent! "
                  + f"You guessed the word: {secret_word}!\n")
            sleep(3)
            print(Style.RESET_ALL + "Wanna try to be hanged again?\n")
            sleep(1)
            play_again()

    if number_mistakes == number_mistakes_allowed:
        print()
        print(Fore.RED + "Poor You! You are dead! "
              + f"The word was: {secret_word}\n")
        sleep(3)
        print()
        print(Style.RESET_ALL + "Wanna be hanged again?\n")
        sleep(1)
        play_again()


def play_again():
    """
    Ask the player if their want to play again or exit
    """
    print(Style.RESET_ALL + "*" * 80)
    print("Choose one of the options:")
    print("1. Play the Game again")
    print("3. Exit\n")
    again_input = input("Enter your option here:\n")

    if again_input == "1":
        welcome()
    elif again_input == "3":
        exit()
    else:
        print(f"You entered: {again_input}. Please enter 1 or 3.\n")
        sleep(2)
        clear()
        play_again()


def rules():
    """
    Shows instructions / rules of the game
    """
    clear()
    print(Fore.YELLOW + "*" * 80)
    print(Fore.YELLOW + "Game Golden Rules:\n")
    print(Style.RESET_ALL
          + "A. You will be guessing the secret word "
          + "by entering single letter at a time.\n"
          + "B. After each incorrectly answered letter "
          + "your Hangman will start to build.\n"
          + "C. You have 7 lifes. When you loose all, "
          + "You will be hang!\n"
          + "D. If you love dying. You can start the game again!\n")
    print(Fore.YELLOW + "*" * 80)
    print(Style.RESET_ALL + "Choose one of the options to continue:")
    print("1. Play the Game")
    print("3. Exit")
    continue_input = input("Enter your option here:\n")

    if continue_input == "1":
        user_name()
    elif continue_input == "3":
        exit()
    else:
        print(f"You entered: {continue_input}. Please enter 1 or 3.\n")
        sleep(2)
        rules()


def exit():
    """
    Goodbye user and end program and start game again
    """
    clear()
    print("*" * 80)
    print("You chose to live longer. Make sure that you enjoy it!\n")
    print(Fore.RED + "GoodBye and Good luck!\n")
    print(Style.RESET_ALL + "*" * 80)
    sleep(5)
    clear()
    welcome()


def main():
    """
    Run all program functions
    """
    clear()
    welcome()
    start_menu()
    user_name()
    game()
    play_again()
    rules()
    exit()


main()
