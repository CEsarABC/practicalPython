from flask import Flask,render_template,session,redirect,url_for,request


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'


@app.route('/', methods=['GET','POST'])
def results():
    return render_template('results0.html')

@app.route('/rules', methods=['GET','POST'])
def rules():
    if request.method == 'POST':
        return redirect(url_for('results'))

    return render_template('results0.html')

if __name__ == '__main__':
    app.run(debug=True)
