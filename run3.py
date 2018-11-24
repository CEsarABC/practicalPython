from flask import Flask,render_template,session,redirect,url_for,request
import string


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

with open('data/riddles2.txt', 'r') as file:
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


############ first definition, first validation, redirecting to next game, user name

@app.route('/', methods=['GET','POST'])
def test_root():
    if request.method == 'POST':
        session['userName'] = request.form['UsernameInput']
        return redirect(url_for('run_index'))
    return render_template('index.html')

############ second definition accessing riddles and taking inputs

@app.route('/show', methods=['GET','POST'])
def run_index():
    if request.method == "POST":
        session['userInput'] = request.form['answerInput']
        userAnswerData = session['userInput']
        for riddle, answer in riddles_list:
            if session['riddle'] == riddle and session['userInput'].lower() == answer:
                session['score'] = session.get('score') + 1

        return redirect(url_for('run_index'))
    else:
        if 'counter' in session:
            session['counter'] = session.get('counter') + 1
            if session.get('counter') == 4 :
                return render_template('results.html')

            #need to add if session[counter]=14 end of the quiz
            #redirect results
        else:
            session['counter'] = 0
            #session['riddle']=riddles[0]
            session['score'] = 0
        #test print(session['counter'])
    # test return 'counter is: {}, the riddle is: {}'.format(session.get('counter'), session.get('riddle'))
        session['riddle']=riddles[session.get('counter')]

        #return redirect(url_for('run_index'))

    return render_template('test.html')

@app.route('/results')
def results():
    # need to clear the session for the next player
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
