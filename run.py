import random

import colorama
from colorama import Fore, Style
from time import sleep

from words import words
from stages import hangman

import os

from pprint import pprint # to be removed later



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
        print(f"You entered: {start_input}. Please enter 1 or 2 or 3.")
        start_input = input("Enter your option here:\n")
        start_game()



def create_user():
    """
    Takes the player name and (in progress)
    """
    clear()
    print("Your gallows is building up...\n")
    sleep(2)
    print("You will enjoy it!\n")
    sleep(2)
    print("In the meantime...")
    user_name_input = input("Enter your name for your gravestone:\n")


def rules():
    """
    Shows instructions / rules of the game
    """
    clear()
    print(Fore.YELLOW + "Game Rules:\n")

    print(Fore.RESET_ALL +
        "A. You will be guessing the secret word by entering single letter at a time.\n"+
        "B. After each incorrectly answered letter your Hangman will start to build.\n"+
        "C. You have 7 lifes. When you loose all, You will be hang!\n"+
        "D. If you love dying. You can start the game again!\n")
    print("*" * 70)
    print("Choose one of the options to continue:")
    print("1. Play the Game")
    print("3. Quit")
    print("*" * 70)
    continue_input = input("Enter your option here:\n")

    if continue_input == "1":
        create_user()
    elif continue_input == "3":
        quit()
    else:
        print(f"You entered: {start_input}. Please enter 1 or 3.")
        continue_input = input("Enter your option here:\n")



def quit():
    """
    Goodbye user and end program
    """
    clear()
    print("You chose to live longer. Make sure that you enjoy it!\n")
    print("GoodBye!\n")
    sleep(5)
    clear()



welcome()
