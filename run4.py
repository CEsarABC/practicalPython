from flask import Flask,render_template,session,redirect,url_for,request


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'


##################### storing data in lists
user_answers = []
riddles_dict = []
riddles = []
answers = []

""" organising the info in separate lists"""""
""" riddles file"""
''' Looking at the gudelines for the project I decided to use file handling
just for reading the text document and create my own lists with this information '''
''' by reading the lines in the txt document I separated the riddles from their
answers and created two lists which then are mix together to create accessable
lists  '''

with open('data/riddles_space.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)

'''joining lists'''

number_of_riddles = len(riddles)
riddles_and_answers = zip(riddles, answers)
riddles_list = list(riddles_and_answers)
#print(riddles_list)


#print(riddles_list[0][1])


"""first definition, first validation, redirecting to next game, user name"""

''' dictionaries acts as a global list to store
the user name and final score for that game - results()'''

dictionaries = []

'''wrong_answers stores the riddle and wrong answer,
just if wrong answer is presented - run_game()'''

wrong_answers = []

'''the first function to take the player name,
show the rules and redirect to the game'''

@app.route('/', methods=['GET','POST'])
def root():
    ''' at the start of the function some sessions are crested
    in order to store information and to cear the sameinformaion
    everytime we start a new game. The list for wrong answers
    is cleaned at the begining of every game  '''
    ''' On the form request I start a counter which will present
    a different riddle, this riddle is in a list and the counter accesses
    the index number, this number increments just if the counter exists
    in session or is more that 0 '''
    ''' this counter helps interacting with the actual session, and is not
    reseted in order to have diferent riddles every turn in the game session '''

    wrong_answers.clear()
    if request.method == 'POST':
        if 'counter' in session and session.get('counter') > 0:
            session['counter'] = session.get('counter') + 1
        session['userName'] = request.form['UsernameInput']
        return redirect(url_for('run_game'))

    else:
        #session['count'] = 0
        session['user'] = ''
        session['score'] = 0
        session['userInput'] = ''

    # if 'counter' in session and session.get('counter') > 0:
    #     session['counter'] = session.get('counter') + 1

    return render_template('index.html')


''' second definition accessing riddles and taking inputs '''

@app.route('/game', methods=['GET','POST'])
def run_game():

    ''' game brings the riddle and a form, this form has an input which will
    on request activate a simple function to compare the user answer to the
    actual answer, using a loop to iterate through a list of tupples created
    previously, if the conditions are both true the score increases'''
    ''' if the answer is wrong the riddle, user answer and actual answer,
    form a dictionary which is appended to a list, in order to acces the
    information later on '''
    ''' just after request the session counter increases to give us the
    next riddle '''

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

    ''' this counters will redirect to results after 3 riddles, every 3 riddles
    there are two blank lines in the text document where the riddles are stored.
     '''
    ''' at the begining the application was jumping every fourth riddle
    and after working on the problem I decided to leave that blank space
    in the txt file  '''

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


    session['riddle']=riddles[session.get('counter')]
        #return redirect(url_for('run_index'))

    return render_template('game.html', dictionaries = dictionaries, wrong_answers=wrong_answers)

@app.route('/results', methods=['GET','POST'])
def results():

    '''test for dictionary'''
    # for entry in dictionaries:
    #     print(entry.get('name'))
    ''' On request, make a new dictionary with the user and the Score
    append to the list for display in leaderboard, after redirect to
    main page to start another game'''

    if request.method == 'POST':
        if 'userName' in session:
            newDict ={
            'name': session['userName'],
            'score': session['score']
            }
            dictionaries.append(newDict)
        return redirect(url_for('root'))

    print(session['counter'])
    return render_template('results.html', dictionaries = dictionaries, wrong_answers=wrong_answers)


if __name__ == '__main__':
    app.run(debug=True)
