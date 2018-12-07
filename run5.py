from flask import Flask,render_template,session,redirect,url_for,request
#import myDictionary
from myDictionary import riddlesExt

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'


##################### storing data in lists
user_answers = []
riddles_dict = []
riddles = []
answers = []

""" organising the info in separate lists"""""
""" riddles file"""

with open('data/riddles_space.txt', 'r') as file:
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

# def user_Information():
#     global total_users
#     if 'user' in session:
#         new_dict = session['userName'] + str(session['count'])
#         new_dict = {
#         "name": "",
#         "score": ""
#         }
#         new_dict['name'] = session['userName']
#         # new_dict['score'] = session.get('score')
#         session['count'] = 0
#         total_users.append(new_dict)
#         session['users'] = total_users
#         # for entry in dictionaries:
#         #     print(['name'])


#print(riddles_list[0][1])


############ first definition, first validation, redirecting to next game, user name
dictionaries = []
wrong_answers = []

@app.route('/', methods=['GET','POST'])
def root():
    wrong_answers.clear()
    if request.method == 'POST':
        session['userName'] = request.form['UsernameInput']
        return redirect(url_for('run_game'))

    else:
        session['count'] = 0
        session['user'] = ''
        session['score'] = 0

    if 'counter' in session and session.get('counter') > 0:
        session['counter'] = session.get('counter') + 1

    return render_template('index.html')


############ second definition accessing riddles and taking inputs

@app.route('/game', methods=['GET','POST'])
def run_game():

    if request.method == "POST":
        session['userInput'] = request.form['answerInput']
        userAnswerData = session['userInput']
        for riddle, answer in riddles_list:
            if session['riddle'] == riddle and session['userInput'].lower() == answer:
                session['score'] = session.get('score') + 1
            else:

                if session['riddle'] == riddle and session['userInput'].lower() != answer:
                    wrong_dict = {
                    'riddle': session['riddle'],
                    'wrongInput': session['userInput'],
                    'realAnswer': riddles_list[session.get('counter')][1]
                    }
                    wrong_answers.append(wrong_dict)

        session['counter'] = session.get('counter') + 1
        print('this is riddle list ' + riddles_list[session.get('counter')][1])
        return redirect(url_for('run_game'))
    else:
        if 'counter' not in session:
            session['counter'] = 0
                #session['riddle']=riddles[0]
            session['score'] = 0


    if 'counter' in session:
        #session['counter'] = session.get('counter') + 1
        if session.get('counter') == 3 :
            return redirect(url_for('results'))
        elif session.get('counter') == 7 :
            return redirect(url_for('results'))
        elif session.get('counter') == 11 :
            return redirect(url_for('results'))
        elif session.get('counter') == 15 :
            session['counter'] = 0
            return redirect(url_for('results')) #make a new start
        elif session.get('counter') == 19 :
            #session['counter'] = 0
            return redirect(url_for('results'))
        # else:
        #     return redirect(url_for('run_index'))

        #need to add if session[counter]=14 end of the quiz
        #redirect results

    session['riddle']=riddles[session.get('counter')]
        #return redirect(url_for('run_index'))

    return render_template('game.html', dictionaries = dictionaries, wrong_answers=wrong_answers)

@app.route('/results')
def results():
    if 'count' in session:
        newDict ={
        'name': session['userName'],
        'score': session['score']
        }
        dictionaries.append(newDict)
###### test for dictionary
    for entry in dictionaries:
        print(entry.get('name'))
    if request.method == 'POST':
        return redirect(url_for('root'))
    # need to clear the session for the next player
    print(session['counter'])
    return render_template('results.html', dictionaries = dictionaries, wrong_answers=wrong_answers)

def clear_session():
    session['score'] = 0
    return None

if __name__ == '__main__':
    app.run(debug=True)
