# Coding in ATOM 1.32.2

## Important Flask testing

https://github.com/CEsarABC/practicalPython

* basic project tree
  - practicalPython
      - data
      - static
      - templates
      - tests
  - run4.py
  - test_run1.py


* In tutorials we can not see any unittest applied to flask.
* the mini project guide is clear on the use of TDD but finding it hard.
* any other suggestions for testing??
* testing cases work in some cases see test_run1.py
  running
  >>python -m unittest test_run1.py

  5 tests ran FAILED (failures=1, errors=1).
  last test case does not find the page results.html. why?
  last test followed same principle but failed
  - [x] taste case for root
  - [x] taste case for game
  - [ ] taste case for results 'not working'

## how to do other tests?
_______________________________________________________________

 ## This is the mini project for practical python

 my idea is to create a web app in which you ask the user for a user name and the user gets directed to the game page where he starts with a question, after the user input his answer this answer is stored just if is wrong and displayed back to the user giving a second chance for the user to answer, if the question is not answered the second time, it continues to the next riddle, keeping score and answers for the session, there are 5 questions in total for game, at the end the user gets redirected to the results page where all the riddles and answers are displayed

 in theory creating an app that can ask a question and create input for answers is easy. I started to create the application in python to see how that might work.
 (testing.py)
 using file handlers I put questions and answers together, loops help me compare the input to the answer for the specific question, after the loop compares gives a message and a score.

 Now using flask Its been challenging, in python the code runs continuously, but html renders code and then stops, how can I render question after question with out changing pages and store the user input at the same time.

 I've seen that in the html any variables stored in memory disappear after loading any other html page, so can't keep scores or user inputs for the session.

 now working with Flask Sessions I can keep the information.

 the challenge is trying to render this python app in the html using flask, in the game.html I'm, trying to bring the loop and render the riddles in the page.

 Using flask sessions managed to be useful as I can display now the riddle and the counter but the challenge is to bring a new riddle with user validation

 new riddles showing after user validation, storing the last answer and trying to display score, score not storing points, probably to the code order
