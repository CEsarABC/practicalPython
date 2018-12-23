# Practical python mini project
This project focuses on flask and how python code can be used to make web applications using logic.

When I was thinking how to implement the game it was clear that I needed to separate the login in sections and link the user activity in the web with the python logic. It is challenging to go back and forth between python, flask and HTML. The application looks simple as it is, but took me a while to figure it out and to understand the complexity of it all.

Cesar's riddle game successfully guides the user through this simple application and uses the technologies to store information and interact with the user in a clean manner.

## Application guidelines
  - [x] Web application that asks players to guess
  - [x] Player is presented with a riddle. Player enters their answer into a form and is submitted
  - [x] If player guesses correctly, they are redirected to the next riddles
  - [x] If player guesses incorrectly, their answer is stored and printed back, text area is cleaned
  - [x] Multiple players can play an instance of the game at the same time
  - [x] Users are identified by their unique user name
  - [x] Leaderboard with scores and players, all recent users

## Project guidelines
  - [x] Logic written in python. other technologies used
  - [x] Semantic HTML
  - [x] Test driven development (see testing section)
  - [x] Use Flask, to structure your project's back render
  - [x] Instructions to deploy (see deployment)
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


## Basic project tree

  - practicalPython
      - data
      - static (css style sheet)
      - templates
      - tests (different manual tests for sections of the application).
      - Wireframes


  - run4.py **(main application)**
  - app.py (copy of the main application for testing only)
  - test_app.py (Unittest for app.py)

## UX
- The application needed to be clean and simple for any user to understand the dynamic of the game. Three sections where created in order to create a path to follow.
- Section one is the introduction where the user gets to understand how the game works. there is a set of rules as guide.
- Section two contains the game where the user clearly sees a layout which is divided in sections and directs the attention to the riddle, invites the user to compete because there is a leaderboard in use where you can see the previous players score and name. The layout brings the riddles with wrong answers and gives a score if the guess is correct.
- Section three shows the final score and the riddles with their answers for the player's amusement. There is an open invitation to try again but this time the riddles will be different, again for the amusement of the player. The leaderboard is kept for other players to see inviting competition
- The design focuses the player with high contrast and expresses hierarchy, with the use of font sizes and expresses dynamics with the use of fonts. Looking  simple but visually appealing.

## Features
- Section one of the application brings a simple model to explain the rules of the game, a form which asks the player for a name and stores the name in a session.
- Section two brings the game where a session counter starts in order to show a different riddle every time the form validates. The leaderboard shows the last players and the bottom section shows the riddles the user could not answer correctly. The form validates with answer or without answer in case the user can not think of an answer.
- Section three shows the results page after 3 riddles, showing the incorrect answered riddles with answers from the dictionary where stored. After validated it saves player's names and score to keep in the leaderboard.
- Redirection to section one will clean the wrong answers but does not re-start the counter used to display the riddles, in order to have a different set of riddles every new game (total of 18 riddles)

### Left to Implement
- [ ] Wanted to bring riddles in random order
- [ ] Writing all sessions to files
- [ ] Creating a data base

## Testing
The testing part of the project is divided into two sections, the unittest and the manual testing.

- Unittest was difficult to implement due to the relation between the material in the course and flask not existing (testing). Unittest was used to test sessions and page responses and not the logic.
  - Files **test_app.py** and **app.py** in the root folder where created to use unittest by modifying the response data in the functions, to check for the existence of sessions in the document
    - **app.py lines (65, 120, 149)**
  - These two test files were left in the root folder of the project after creating path problems when being used inside the test folder
  - to run test_app.py in root folder `$ python test_app.py`
  - to run tests in dictionary `$python test_dictionary.py`  and
  `$python testing_file_handles.py`


- Manual tests were employed in the **test** folder within the project and they are testing the logic in the python code
  - **testing_dictionary.py** was created to test the logic in inputs storage and the use of sessions to make new dictionaries
  - **testing_file_handles.py** was created to test the use of file handles, reading from a file and creating lists and dictionaries with the test file. testing assertions with user input


- Other tests include the HTML test by running the application locally and checking for issues in the layouts of the different pages.

- Tests for Bootstrap and media queries for mobile devices, readability and organization of columns and rows

- Tested in mobile devices, tablets, laptops and pcs.

- Tested in all devices after Heroku deployment


## Deployment
- Project fully deployed to Heroku  https://practical-project.herokuapp.com/
  - The project was deployed following the guidelines from the code academy materials
  - Working in virtual environment
  - New project was created in Heroku
  - requirements.txt was created
  - Procfile was created
  - Heroku remote was set in order to push application
  - Configuration variables were changed as indicated to have 'IP' = (0.0.0.0) and 'PORT' = (5000)


- To run this code locally I have some lines of code, one to use in cloud9 and one to use in any other IDE like Atom which I used when not connected to the internet

- The last Python version enabled for cloud9 was installed **Python-3.6.2** in order to create the virtual environment based on it. Code taken from https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

- My project in cloud9 had the pip module updated to the last version and the module **virtualenv** installed to manage my environment
- After the environment was created based on python3.6 flask was installed

- Requirements.txt
    - Click==7.0
    - Flask==1.0.2
    - itsdangerous==1.1.0
    - Jinja2==2.10
    - MarkupSafe==1.1.0
    - Werkzeug==0.14.1

**Running locally - in the terminal**
- To run this application outside the virtual environment `$ python3 run4.py`
- To activate the virtual environment `$ source env/bin/activate`
- To run this application inside the virtual environment `$ python run4.py`

## Credits

- Some samples where taken from http://flask.pocoo.org/docs/0.12/testing/ for testing flask sessions
- This module was complemented through a couple of courses from **Udemy**
  - Automated software testing with python
  - Python and Flask bootcamp

## Media
- Fonts taken from google fonts
- No other external media used

## Acknowledgments
Thank you to the code institute for the support. This last project has been challenging and took me some time to develop. I have learned a lot and I hope to keep learning to become the professional I want to be.
Thank you to the slack channels for the support and the code academy tutors which always had answers to help me move forward.
