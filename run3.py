from flask import Flask,render_template,session,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
user_list = []

def new_user():
    print('this function needs to take a name and putting in a list')
    for i in range(0,2):
        user = input('this is my name: ')
        user_list.append(user)
    print(user_list)

# new_user()
user_answers = []
riddles_dict = []
riddles = []
answers = []



with open('data/riddles1.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)


number_of_riddles = len(riddles)
riddles_and_answers = zip(riddles, answers)
riddles_list = list(riddles_and_answers)

class RiddleForm(FlaskForm):
    answer = StringField('Please insert your Answer: ', validators=[DataRequired()])
    submit = SubmitField('Ok')



@app.route('/show', methods=['GET','POST'])
def test_index():
    if 'counter' in session:
        session['counter'] = session.get('counter') + 1
        session['riddle']=riddles[session.get('counter')]
    else:
        session['counter'] = 0
        session['riddle']=riddles[0]
    #return 'counter is: {}, the riddle is: {}'.format(session.get('counter'), session.get('riddle'))


    form = RiddleForm()

    if form.validate_on_submit():

        return redirect('show')
    return render_template('test.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
