import random

import colorama
from colorama import Fore, Style
from time import sleep

from words import words
from stages import hangman

import os

from pprint import pprint



def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """
    Welcome message
    """
    print('*' * 70)
    print(Fore.YELLOW + "Welcome to the Hangman Game!\n")
    print(Fore.RED + "Do you know how you want to hang today?\n")
    print(Style.RESET_ALL + '*' * 70)
    print(Fore.RED + '  +---+'+'  +---+'+'  +---+')
    print(Fore.RED + '  |   |'+'  |   |'+'  |   |')
    print(Fore.RED + '  O   |'+'  O   |'+'  O   |')
    print(Fore.RED + ' /|\  |'+' /|\  |'+' /|\  |')
    print(Fore.RED + ' / \  |'+' / \  |'+' / \  |')
    print(Fore.RED + '      |'+'      |'+'      |')
    print(Fore.GREEN + '========='+'========='+'=========')
    print(Style.RESET_ALL + '*' * 70)
    sleep(3)



welcome()



