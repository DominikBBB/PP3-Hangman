<p align="center"> <img src="assets/pictures/AmIResponsive-03.png" alt="Mockup of the hangman game" /> </p>


# The Hangman Game

## by DB

---

---

This is my Portfolio Project 3 (PP3) which is a part of the Code Institute’s Full Stack Software Development Diploma Course. This project demonstrates the skills and knowledge of the Python Programming Language which I have learned during the course.
The project purpose is to build a command-line python application that allows user to manage a common dataset about a particular domain.

#### [--- Click here to view the site ---](https://pp3-hangman-db.herokuapp.com/)
#### [--- Click here to view the repository ---](https://github.com/DominikBBB/PP3-Hangman)

---

# Table of Contents:

1. [Project Overview](#project-overview)
2. [User Experience(UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
        - [Flowchart](#flowchart)
    - [Skeleton](#skeleton)
        - [Mockups](#mockups)
    - [Surface](#surface)
        - [Typography](#typography)
3. [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
4. [Technologies](#technologies)
    - [Main Languages](#main-languages)
    - [Python Libraries](#python-libraries)
    - [Other Technologies](#other-technologies)
    - [Resources](#Resources)
5. [Testing](#testing)
    - [Validation](#validation)
    - [Funcionality testing](#funcionality-testing)
    - [User Stories testing](#user-stories-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
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


## User Stories:

- As a user:

    1. I would like the game to be easy to navigate,
    2. I would like to easily understand the rules,
    3. I would like to enter my name,
    4. I would like to be warmed if I put incorrent character,
    5. I would like to track the game progress,
    6. I would like to have a chance to retake the game.

- As a site creator:

    7. I want to make that game with user-friendly and intuitive navigation,
    8. I want to make sure that the game rules are easily to understand,
    9. I want to ensure the game level is average enough to prevent any user from becoming bored,
    10. I want user to be able to choose to play again or exit. 


[Back to Table Of Contents](#table-of-contents)


## Strategy:

### Customer Goals:

   1. Enjoying the time when playing the game,
   2. Easy to understand and navigate,
   3. Checking the knowledge.

### Business Goals:

   1. Create a useful application with clear and understandable objectives,
   2. Develop the game with user-friendly and intuitive navigation.


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
    <p>&nbsp;</p>

    <details><summary>Main Menu Screenshot 1</summary>

    ![MM](assets/testing/manual/MT-01.png)

    </details>
    <details><summary>Main Menu Screenshot 2</summary>

    ![MM](assets/testing/manual/MT-02.png)

    </details>
    <p>&nbsp;</p>

2. Player Name:
    - player name input is displayed
    <p>&nbsp;</p>

    <details><summary>Player Name Input Screenshot 1</summary>

    ![PNI](assets/testing/manual/MT-03.png)

    </details>
    <details><summary>Player Name Input Screenshot 2</summary>

    ![PNI](assets/testing/manual/MT-04.png)

    </details>
    <p>&nbsp;</p>

3. Instructions / Rules:
    - instructions on how to use the program are displayed
    - gives user 2 options to select: start the game or exit
    - user is prompt to choose only one of these 2 options
    <p>&nbsp;</p>

    <details><summary>Instructions Screenshot</summary>

    ![I](assets/testing/manual/MT-10.png)

    </details>
    <p>&nbsp;</p>

4. Enter the letter:
    - ask user to enter the single letter
    <p>&nbsp;</p>

    <details><summary>Enter The Letter Screenshot 1</summary>

    ![ETL](assets/testing/manual/MT-05.png)

    </details>
    <details><summary>Enter The Letter Screenshot 2</summary>

    ![ETL](assets/testing/manual/MT-06.png)

    </details>
    <details><summary>Enter The Letter Screenshot 3</summary>

    ![ETL](assets/testing/manual/MT-07.png)

    </details>
    <p>&nbsp;</p>

5. The end of the game and the game loop
    - message with the end result and secret word
    - ask user if they want to play again or exit
    - user is prompt to choose only one of these 2 options
    <p>&nbsp;</p>

    <details><summary>End of the Game Screenshot 1</summary>

    ![GO](assets/testing/manual/MT-08.png)

    </details>
    
    <details><summary>End of the Game Screenshot 2</summary>

    ![GO](assets/testing/manual/MT-09.png)

    </details>
    <p>&nbsp;</p>

6. Exit Game
    - Goodbye and Good Luck message
    <p>&nbsp;</p>

    <details><summary>Exit Game Screenshot</summary>

    ![EG](assets/testing/manual/MT-11.png)

    </details>
    <p>&nbsp;</p>

## Future Features:

- User will be able to choose level of difficulty,
- User will be able to enter own word.


[Back to Table Of Contents](#table-of-contents)


---


# Technologies:

## Main Languages:

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - is a high-level, general-purpose programming language,
- [Markdown](https://en.wikipedia.org/wiki/Markdown) - markup language used to write README and TESTING documents.

## Python Libraries:

- [random](https://docs.python.org/3/library/random.html) - built-in python module - used to generate random quote and random book on exit screen,
- [textwrap](https://docs.python.org/3/library/textwrap.html) - built-in python module - used to wrap lines over 79 char to next line e.g. long book description,
- [os](https://docs.python.org/3/library/os.html) - built-in pythod module - used to write clear_terminal function,
- [colorama](https://pypi.org/project/colorama/) - used to color terminal outputs,
- [time&sleep](https://docs.python.org/3/library/time.html) - used to displayed delayed messages in the terminal.

## Other Technologies:

- [Gitpod](https://gitpod.io/) - used to write the project code,
- [Visual Studio Code](https://code.visualstudio.com/) - used to write the project code,
- [Git]() - used for code version control after git-push command to GitHub,
- [GitHub](https://github.com/) - used to store the project's code,
- [Responsive Design](http://ami.responsivedesign.is/) - used to do responsive mockups,
- [LucidChart](https://www.lucidchart.com/) - used to create flow chart diagram,
- [Heroku](https://id.heroku.com/) - online app used to deploy project,
- [CI-Python-Linter](https://pep8ci.herokuapp.com/) - PEP8 Python Validator,
- [Grammarly](https://www.grammarly.com/) - used to help with grammar check.

## Resources:

- [Code Institute Course Content](https://learn.codeinstitute.net/dashboard) - main source of fundamental knowledge,
- [Code Institute SLACK Community](https://slack.com/) - source of assistance,
- [Code Institute Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) - CI student template for deploying PP3 project,
- [Wikipedia](https://pl.wikipedia.org/) - content and links,
- [Grammarly](https://app.grammarly.com/) - help with grammar and typo check,
- [GitHub Community](https://github.com/) - source of information, solutions and suggestions,
- [Stack Overflow](https://stackoverflow.com/) - source of knowledge,
- [Flake8 Rules](https://www.flake8rules.com/) - The Big Ol' List of Rules - Python Code Style,
- [Python Enhancement Proposals](https://peps.python.org/) - source of knowledge,
- [Fabio Musanni's YT Tutorial](https://youtu.be/lJ7RhvNvsnc).

  
[Back to Table Of Contents](#table-of-contents)


---


# Testing:

## Validation:


   [CI-Python-Linter](https://pep8ci.herokuapp.com/) was used to check the code for errors. Code passed validation in all files. Only warning 'W605 invalid escape sequence "\" ' showed up related to the hangman ascii art code which doesn't effect working code. Attempts to resolve the warning ended unsucesful.

   [Validation](assets/testing/pep8/VALIDATION.md)
   

   
## Funcionality Testing:


   The functional final test was carried out using a flowchart. All works as expected. No bugs found.

   [Functional testing](assets/testing/manual/FUNCIONAL.md)


## User Stories Testing:


   1. I would like the game to be easy to navigate.

        There is implemented a simple and clear user interface that guide the user through the game.

   2. I would like to easily understand the rules.

        There are clear and concise instructions provided at the beginning of the game.

   3. I would like to enter my name.

        User puts their name after he decided to play the game. In the meantime, he is informed that his gallows is building up.

   4. I would like to be warmed if I put incorrent character.

        There is an error messages and visual cues to indicate that there has been an error. the user is prompt to input correct data before continuing.

   5. I would like to track the game progress.

        There is a meter of 'wrong letters', 'guesses left' and progress of the gallow.

   6. I would like to have a chance to retake the game.

        The user is clearly asked at the end of the game if he wants to play again or exit program.

   7. I want to make that game with user-friendly and intuitive navigation.

        Terminal has black background. Letters are white, red and yellow. High contrast makes all options, commands well seen and easy to navigate.

   8. I want to make sure that the game rules are easily to understand.

        Four Game Golden Rules are short and easy to understand.

   9. I want to ensure the game level is average enough to prevent any user from becoming bored.

        Secret words are animals names and each consists of 4 letters. In future features, the user will be able to choose level of difficulty, and enter his own word.

   10. I want user to be able to choose to play again or exit.
        
        The user is clearly asked at the end of the game if he wants to play again or exit program.


## Bugs and Fixes









[Back to Table Of Contents](#table-of-contents)


---


# Deployment:

## Heroku:

The project was deployed using Heroku by the following steps:

1. Create or log in to your account at heroku.com
2. Click 'New' -> 'Create new app'
3. Type in the app name (current project name is 'pp3-hangman-db') -> select the region -> 'Create app'
4. Navigate to 'Settings' tab
5. Click 'Reveal Config Vars' -> Add key: 'PORT' and value: '8000'
6. Then click 'Add buildpack' -> add 'python' -> add 'nodejs'
7. Navigate to 'Deploy' tab
8. Select 'GitHub' in the 'Deployment method' area
9. Enter the GitHub repository name in the search bar -> 'Connect'
10. Click 'Deploy Branch' and wait for it to be built


## GitHub pages:

The steps to deploy via GitHub pages:

1. Log into Github account,
2. Navigate to the [Repository](https://github.com/DominikBBB/PP3-Hangman),
3. Click the 'Settings' option at the top of the repository,
4. Click the 'Pages' option on the left-hand menu, located near the bottom,
5. Within the 'Source' tab Select the drop-down titled 'None',
6. Select the branch named 'main' (in some cases it can be named 'Master'),
7. Click 'Save',
8. You will be prompted with a URL to your deployed site,
9. Site deployed.

When the above steps have been completed, it can sometimes take a moment for the deployed URL to update. It is enough to refresh the page until the site is fully deployed.


## Forking The GitHub Repository:

To use this code and make changes without affecting the original code you can do what is called 'Forking the repository'. By forking this repository you are given a copy of the code at that moment in time that you can use freely. To fork this repository you need to follow the following few steps:

1. Log into your GitHub account,
2. Navigate to the [Repository](https://github.com/DominikBBB/PP3-Hangman), you are willing to fork,
3. In the upper-right of the repository, click the 'Fork' button,
4. A copy of the Repository will now be available within your repositories.

You will now have a copy of the code available to clone and work on without affecting the original code.


## Cloning the Project:

To make a local clone of the project follow these steps:

1. Log into your GitHub account.
2. Navigate to the [Repository](https://github.com/DominikBBB/PP3-Hangman),
3. In the upper section of the repository click the drop-down named 'Code',
4. Copy the SHH address,
5. Open GitBash,
6. Navigate to the correct directory,
7. Create a new directory named 'PP3-Hangman-Clone',
8. CD into 'PP3-Hangman-Clone',
9. Enter 'git clone SSH_ADDRESS',
10. GitBash will clone the repository into this directory,
11. enter 'code .'.

  
[Back to Table Of Contents](#table-of-contents)


---

# Credits:

- [Code Institute Course Content](https://learn.codeinstitute.net/dashboard) - Lines of code from walkthrough projects,
- [GitHub Community](https://github.com/) - suggestions for lines of code, project's file structure, and descriptions in readme,
- [Stack Overflow](https://stackoverflow.com/) - suggestions for lines of code,
- [Fabio Musanni's YT Channel](https://www.youtube.com/@FabioMusanni),
- [Code Institute SLACK Community](https://slack.com/) - Source of assistance,

  
[Back to Table Of Contents](#table-of-contents)


---


# Acknowledgments:

I would like to thank:

- My mentor Chris Quinn for his helpful and valuable feedback and guidance and great support,
- Friends and family for helping me with testing and mental support.


[Back to Table Of Contents](#table-of-contents)