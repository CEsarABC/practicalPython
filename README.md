# Practical python mini project
This project focuses in flask and how python code can be used to make web applications using logic.

when I was thinking how to implement the game it was clear that I needed to separate the login in sections and link the user activity in the web with the python logic. it is challenging to go back and forth between python, flask and HTML. the application looks simple as it is but took me a while to figure it out, to understand the complexity of it all.

Cesar's riddle game successfully guides the user through this simple application and uses the technologies to store information and interact with the user in a clean manner.

## Application guidelines
  - [x] Web application that asks players to guess
  - [x] player is presented with a riddle. Player enter their answer into a form and is submitted
  - [x] if player guesses correctly, they are redirected to the next riddles
  - [x] If player guesses incorrectly, their answer is stored and printed back, text area is cleaned
  - [x] multiple players can play an instance of the game at the same time
  - [x] Users are identified by their unique user name
  - [x] leaderboard with scores and players, all recent users

## Project guidelines
  - [x] Logic written in python. other technologies used
  - [ ] semantic HTML
  - [x] Test driven development (see testing section)
  - [x] Use Flask, to structure your project's back render
  - [x] instructions to deploy (see deployment)
  - [x] Make sure the site is responsive
  - [x] User stories, wireframes
  - [x] CSS and Bootstrap frameworks used
  - [x] README.md file made
  - [x] GitHub version control used during development
  - [x] Final version of the code deployed in Heroku



## Technologies used
- HTML
- CSS
- Bootstrap 4.0
- Python 3.6
 - Virtualenv (virtual environment)
 - Unittest
- Flask
- ATOM 1.32.2 (for offline coding)

At the beginning of this project cloud9 presented challenges in the way it uses different versions of python, creating a virtual environment was a great move because the deployment to heroku was pretty easy.


## basic project tree

  - practicalPython
      - data
      - static (css style sheet)
      - templates
      - tests (different manual tests for sections of the application).


  - run4.py (main application)
  - app.py (copy of the main application for testing only)
  - test_app.py (Unittest for app.py)

## UX
- The application needed to be clean and simple for any user to understand the dynamic of the game, three sections where created in order to create a path to follow.
- the section one is the introduction where the user gets to understand how the game works. there is a set of rules as guide.
- section two contains the game where the user clearly sees a layout which is divided in sections and directs the attention to the riddle, invites the user to compete because there is a leaderboard in use where you can see the previous players score and name. the layout brings the riddles with wrong answers and gives a score if the guess is correct.
- section three brigs the final score and the riddles with their answers for the player's amusement. there is an open invitation to try again but this time the riddles will be different, again for the amusement of the player
- leaderboard is kept for other players to see inviting competition
- the design focuses the player with high contrast and expresses hierarchy with the use of fonts sizes and expresses dynamism with the use of fonts. looking for simplicity but visual appeal.

## Features
- Section one of the application brings a simple modal to explain the simple rules of the game, a form which asks the player for a name and stores the name in a session
- Section two brings the game where an session counter starts in order to show a different riddle every time the form validates. leaderboard shows the last players and the bottom section brings the riddles the user could not answer correctly. the form validates with answer or without answer in case the user can not think of an answer.
- Section three brigs the results page after 3 riddles, brings the incorrect answered riddles with answers from the dictionary where stored. After validated saves player's name and score to keep in the leaderboard.
- Redirection to section one will clean the wrong answers but does not re start the counter used to display the riddles, in order to have a different set of riddles every new game (total of 18 riddles)

### Left to Implement
- [ ] wanted to bring riddles in random order
- [ ] writing all sessions to files
- [ ] creating a data base

## Testing
Testing part if the project is divided into two sections, the unittest and the manual testing.

- Unittest was difficult to implement due to the relation between the material in the course and flask is not existent(testing), Unittest was used to test sessions and page responses and no the logic.
  - files **test_app.py** and **app.py** where created to use unittest by modifying the response data in the functions, to check for the existence of sessions in the document
    - **app.py lines (65, 120, 149)**
  - these two tests files where left in the root folder of the project after creating path problems when being used inside test folder

- Manual tests where employed in the test folder within the project and they are testing the logic in the python code
  - **testing_dictionary.py** was created to test the logic in inputs storage and the use of session to make new dictionaries
  - **testing_file_handles.py** was created to test the use of file handles, reading from a file and creating lists and dictionaries with the test file. testing assertions with user input

- Other tests include the HTML test by running the application locally and checking for issues in the layouts of the different pages.

- tests for Bootstrap and media queries for mobile devices, readability and organization of columns and rows

- tested in mobile devices, tablets, laptops and pcs.

- tested in all devices after Heroku deployment
