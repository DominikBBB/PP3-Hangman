import random

import colorama
from colorama import Fore, Style

from words import words
from stages import hangman

import os

from pprint import pprint



def welcome():
    """
    Welcome message
    """
    print('*' * 70)
    print(Fore.YELLOW + "Welcome to the Hangman Game!\n")
    print(Fore.RED + "How do you want to hang today?\n")
    print(Style.RESET_ALL + '*' * 70)
    print('  +---+'+'  +---+'+'  +---+')
    print('  |   |'+'  |   |'+'  |   |')
    print('  O   |'+'  O   |'+'  O   |')
    print(' /|\  |'+' /|\  |'+' /|\  |')
    print(' / \  |'+' / \  |'+' / \  |')
    print('      |'+'      |'+'      |')
    print(Fore.GREEN + '========='+'========='+'=========')
    print('*' * 70)


welcome()



