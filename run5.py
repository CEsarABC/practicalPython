from flask import Flask,render_template,session,redirect,url_for,request
import myDictionary
from myDictionary import riddlesExt

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'


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
total_users = []

def user_Information():
    global total_users
    if 'user' in session:
        new_dict = session['userName'] + str(session['count'])
        new_dict = {
        "name": "",
        "score": ""
        }
        new_dict['name'] = session['userName']
        # new_dict['score'] = session.get('score')
        session['count'] = 0
        total_users.append(new_dict)
        session['users'] = total_users
        print(new_dict)





############ first definition, first validation, redirecting to next game, user name
dictionaries = []
@app.route('/', methods=['GET','POST'])
def test_root():

    if request.method == 'POST':
        session['userName'] = request.form['UsernameInput']
        return redirect(url_for('run_index'))

    else:
        session['count'] = 0
        session['user'] = ''
        session['score'] = 0
    return render_template('index.html')


############ second definition accessing riddles and taking inputs

@app.route('/game', methods=['GET','POST'])
def run_index():
    if request.method == "POST":
        session['userInput'] = request.form['answerInput']
        userAnswerData = session['userInput']
        for riddle, answer in riddles_list:
            if session['riddle'] == riddle and session['userInput'].lower() == answer:
                session['score'] = session.get('score') + 1

        return redirect(url_for('run_index'))

    # elif request.method == "POST" and request.form['answerInput'] == None:
    #
    #     return redirect(url_for('run_index'))

    else:
        if 'counter' in session:
            session['counter'] = session.get('counter') + 1
            if session.get('counter') == 3 :
                return redirect(url_for('results'))
            elif session.get('counter') == 7 :
                return redirect(url_for('results'))
            elif session.get('counter') == 11 :
                return redirect(url_for('results'))
            elif session.get('counter') == 15 :
                return redirect(url_for('results'))
            # else:
            #     return redirect(url_for('run_index'))

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

    return render_template('game.html', dictionaries = dictionaries)

@app.route('/results')
def results():
    if 'count' in session:
        newDict ={
        'name': session['userName'],
        'score': session['score']
        }
        dictionaries.append(newDict)
    if request.method == 'POST':
         # del session['counter'] #### delete the session here
         return redirect(url_for('run_index'))
    # need to clear the session for the next player
    return render_template('results.html', dictionaries = dictionaries)

def clear_session():
    session['score'] = 0
    return None

if __name__ == '__main__':
    app.run(debug=True)
