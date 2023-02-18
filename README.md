<p align="center"> <img src="assets/pictures/AmIResponsive-03.png" alt="Mockup of the hangman game" /> </p>


# The Hangman Game

## by DB

---

---

This is my Portfolio Project 3 (PP3) which is a part of the Code Institute’s Full Stack Software Development Diploma Course. This project demonstrates the skills and knowledge of the Python Programming Language which I have learned during the course.
The project purpose is to build a command-line python application that allows user to manage a common dataset about a particular domain.

#### [Click here to view the site.](https://pp3-hangman-db.herokuapp.com/)
#### [Click here to view the repository.](https://github.com/DominikBBB/PP3-Hangman)

---

# Table of Contents:

1. [Project Overview](#project-overview)
2. [User Experience(UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
        - [Flowchart](#flowchart)
    - [Skeleton](#skeleton)
        - [Mockups](#mockups)
    - [Surface](#surface)
        - [Typography](#typography)
3. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features](#future-features)
4. [Technologies](#technologies)
    1. [Languages](#languages)
    2. [Other Technologies](#other-technologies)
    3. [Resources](#Resources)
5. [Testing](#testing)
    1. [Tests](#tests)
        1. Functionality testing
        2. Compatibility testing and Responsiveness
        3. Performance testing
        4. [Visual testing](#visual-testing)
        5. [Funcionality testing](#funcionality-testing)
        6. [Testing User Stories](#testing-user-stories)
    2. [Bugs and Fixes](#bugs-and-fixes)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgments](#acknowledgments)


---


# Project Overview:

The Hangman Game is a very popular world game. In this application, the user is asked to input their name, and then a random secret word is choosen from a list of words. The user has to guess the word by inputting letters one at a time. If the letter is in the word, it is revealed, but if it is not, the player is penalized with an additional body part in the gallows. If the user correctly guesses full word, the app will ask the player if they want to try to be hanged  again. If the player does not guess the word correctly within the allowed number of guesses, the app will reveal the answer and ask the player if they want to be hanged again. The user has 7 lifes. The application is very easy to navigate for anybody.

[Back to Table Of Contents](#table-of-contents)


---


# User Experience UX:

## Target Audience:

- People of all ages.

[Back to Table Of Contents](#table-of-contents)


## Strategy:

### Business Goals:

1. I want to make that game with user-friendly and intuitive navigation,
2. I want to make sure that the game rules are easily to understand,
3. I want to ensure the game level is average enough to prevent any user from becoming bored,
4. I want user to be able to choose to play again or exit. 

### Customer Goals:

1. I would like the game to be easy to navigate,
2. I would like to easily understand the rules,
3. I would like to enter my name,
4. I would like to be warmed if I put incorrent character,
5. I would like to track the game progress,
6. I would like to have a chance to retake the game.


[Back to Table Of Contents](#table-of-contents)


## Scope:

#### The scope of the hangman game in its first release is defined by the following features:

- a simple, error-free game,
- clean user interface for easy navigation and readability,
- clear program response to the user input,
- non-bulky text. 

#### Features that are to be considered for future releases:

- to choose level of difficulty,
- to be able to enter own word.


[Back to Table Of Contents](#table-of-contents)


## Structure:

### Flowchart

The flow chart showing the logic of the program can be found here:

<details><summary>Flowchart</summary>

![Flowchart](assets/flowchart/PP3-Hangman-Flowchart.png)

</details>


[Back to Table Of Contents](#table-of-contents)


## Skeleton:

### Mockups:

<details><summary>Mockups</summary>

![MockUps](assets/pictures/AmIResponsive-03.png)

</details>


[Back to Table Of Contents](#table-of-contents)


## Surface:

### Typography:

Topography in the terminal is very limited. To make the terminal messages more intuitive Colorama colors were introduced. The incorrect answers and gallows are in red, game golden rules in yellow and the grass is green.


[Back to Table Of Contents](#table-of-contents)


---


# Features:

## Existing Features:

1. Main Menu:
    - welcome message is displayed
    - gives user 3 options to select: start the game, read the rules or exit
    - user is prompt to choose only one of these 3 options

    <details><summary>Main Menu Screenshot 1</summary>

    ![MM](assets/testing/manual/MT-01.png)

    </details>
    <details><summary>Main Menu Screenshot 2</summary>

    ![MM](assets/testing/manual/MT-02.png)

    </details>


2. Player Name:
    - player name input is displayed

    <details><summary>Player Name Input Screenshot 1</summary>

    ![PNI](assets/testing/manual/MT-03.png)

    </details>
    <details><summary>Player Name Input Screenshot 2</summary>

    ![PNI](assets/testing/manual/MT-04.png)

    </details>

3. Instructions / Rules:
    - instructions on how to use the program are displayed
    - gives user 2 options to select: start the game or exit
    - user is prompt to choose only one of these 2 options

    <details><summary>Instructions Screenshot</summary>

    ![I](assets/testing/manual/MT-10.png)

    </details>

4. Enter the letter:
    - ask user to enter the single letter

    <details><summary>Enter The Letter Screenshot 1</summary>

    ![ETL](assets/testing/manual/MT-05.png)

    </details>
    <details><summary>Enter The Letter Screenshot 2</summary>

    ![ETL](assets/testing/manual/MT-06.png)

    </details>
    <details><summary>Enter The Letter Screenshot 3</summary>

    ![ETL](assets/testing/manual/MT-07.png)

    </details>

5. The end of the game and the game loop
    - message with the end result and secret word
    - ask user if they want to play again or exit
    - user is prompt to choose only one of these 2 options

    <details><summary>End of the Game Screenshot 1</summary>

    ![GO](assets/testing/manual/MT-08.png)

    </details>
    
    <details><summary>End of the Game Screenshot 2</summary>

    ![GO](assets/testing/manual/MT-09.png)

    </details>

6. Exit Game
    - Good bye and good luck message

    <details><summary>End of the Game Screenshot 2</summary>

    ![EG](assets/testing/manual/MT-11.png)

    </details>


## Future Features:

- to choose level of difficulty,
- to be able to enter own word.


[Back to Table Of Contents](#table-of-contents)


---