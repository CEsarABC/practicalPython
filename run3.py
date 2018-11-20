from flask import Flask,render_template,session,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,SelectField,TextField,TextAreaField,SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

################### not in use
user_list = []

def new_user():
    print('this function needs to take a name and putting in a list')
    for i in range(0,2):
        user = input('this is my name: ')
        user_list.append(user)
    print(user_list)

##################### storing data in lists
user_answers = []
riddles_dict = []
riddles = []
answers = []

########### organising the info in separate lists

with open('data/riddles1.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)

########### joining lists

number_of_riddles = len(riddles)
riddles_and_answers = zip(riddles, answers)
riddles_list = list(riddles_and_answers)
#print(riddles_list)
############## creating forms for validation

class InfoForm(FlaskForm):
    userName = StringField('Please insert your Nickname: ', validators=[DataRequired()])
    submit = SubmitField('Ok')

class RiddleForm(FlaskForm):
    answer = StringField('Please insert your Answer: ', validators=[DataRequired()])
    submit = SubmitField('Ok')

############ first definition, first validation, redirecting to next game, user name

@app.route('/', methods=['GET','POST'])
def test_root():
    form = InfoForm()
    if form.validate_on_submit():
        session['userName'] = form.userName.data
        return redirect(url_for('test_index'))
    return render_template('index.html',form=form)

############ second definition accessing riddles and taking inputs

@app.route('/show', methods=['GET','POST'])
def test_index():
    form = RiddleForm()
    if request.method == "POST":
        if form.validate_on_submit():
    ##### issue not comparing answer comparing wrong riddle
            session['userInput'] = form.answer.data

            for riddle, answer in riddles_list:
                # test print(session['riddle'], answer, session['userInput'])
                if session['riddle'] == riddle and session['userInput'] == answer:
                    session['score'] = session.get('score') + 1
                # else:
                #     return(session['riddle'])
            return redirect(url_for('test_index'))
    else:
        if 'counter' in session:
            session['counter'] = session.get('counter') + 1
            #need to add if session[counter]=14 end of the quiz
            #redirect results
        else:
            session['counter'] = 0
            #session['riddle']=riddles[0]
            session['score'] = 0
        #test print(session['counter'])
    #return 'counter is: {}, the riddle is: {}'.format(session.get('counter'), session.get('riddle'))
        session['riddle']=riddles[session.get('counter')]

        #return redirect(url_for('test_index'))


    return render_template('test.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
