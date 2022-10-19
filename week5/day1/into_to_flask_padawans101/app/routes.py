from app import app
from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/signup')
def signMeUp():
    form = UserCreationForm()




    return render_template('signup.html', x = form)