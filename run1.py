from flask import Flask,render_template,session,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

user_answers = []
riddles_dict = []
riddles = []
answers = []

# Accessing the riddles to pick questions and answers

with open('data/riddles1.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)


# function to bring the riddles and answers into a list to compare the guess answer
# and give score, storing the answer if is wrong to print back


number_of_riddles = len(riddles)
riddles_and_answers = zip(riddles, answers)
riddles_list = list(riddles_and_answers)
