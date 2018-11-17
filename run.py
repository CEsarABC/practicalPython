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

class InfoForm(FlaskForm):
    userName = StringField('Please insert your Nickname: ', validators=[DataRequired()])
    submit = SubmitField('Ok')

class RiddleForm(FlaskForm):
    answer = StringField('Please insert your Answer: ', validators=[DataRequired()])
    submit = SubmitField('Ok')


@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['userName'] = form.userName.data
        return redirect(session['userName'])
    return render_template('index.html', form=form)

@app.route('/<userName>', methods=["GET","POST"])
def game(userName):
    score = 0
    riddle = ''
    # for riddle, answer in riddles_list:
    #     guess_answer = input(riddle+"\n" + '>>')
    #     if guess_answer == answer:
    #         score += 1
    #         right_message = ('Right!')
    #     else:
    #         user_answers.append(guess_answer)
    #         wrong_message = ('Wrong! ' + 'the answer is >> ' + answer)
    #         score_points = (' you got {0} correct out of {1}'.format(score, number_of_riddles))

    form = RiddleForm()
    if form.validate_on_submit():
        session['userName'] = form.userName.data
        #return redirect(session['userName'])
    return render_template('game.html',form=form, riddle=riddle, score=score)



if __name__ == '__main__':
    app.run(debug=True)
