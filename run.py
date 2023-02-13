import random

import colorama
from colorama import Fore

from words import words
from stages import hangman

import os

from pprint import pprint



def welcome():
    """
    Welcome message
    """
    print('*' * 70)
    print("Welcome to the Hangman Game!\n")
    print("How do you want to hang today?\n")
    print('*' * 70)
    print('  +---+'+'  +---+'+'  +---+')
    print('  |   |'+'  |   |'+'  |   |')
    print('  O   |'+'  O   |'+'  O   |')
    print(' /|\  |'+' /|\  |'+' /|\  |')
    print(' / \  |'+' / \  |'+' / \  |')
    print('      |'+'      |'+'      |')
    print('========='+'========='+'=========')
    print('*' * 70)







welcome()



