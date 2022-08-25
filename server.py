from flask import Flask, render_template, request, redirect, session
from random import randint


app = Flask(__name__)
app.secret_key = 'this ones for the memories'


@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = randint(1,100)
    if 'count' not in session:
        session['count'] = 0

    return render_template('index.html', sesh=session)


@app.route('/guess', methods=['POST'])
def process_guess():

    response = int(request.form['guess'])
    session['response'] = response
    if session['count'] <= 4:
        if response == session['answer']:
            session['result'] = 'correct'
        elif response > session['answer']:
            session['result'] = 'high'
        else:
            session['result'] = 'low'
    else:
        session['result'] = 'lose'

    session['count'] += 1
    return redirect('/')

@app.route('/reset_game')
def reset_game():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)