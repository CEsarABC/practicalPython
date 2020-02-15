import os
from flask import Flask,render_template,session,redirect,url_for,request


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'

def testFile():
    if os.path.exists('./texts.txt'):
        with open('texts.txt', 'r') as file:
            text = file.read()
        print(text)
        print(type(text))
        print('file is on')
    else:
        print('not recognised')

testFile()

''' To run in Atom (offline)'''
if __name__ == '__main__':
    app.run(debug=True)
