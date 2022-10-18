from app import app
from flask import render_template

@app.route('/')
def homePage():
    people = ['shoha', 'brandt', 'blair']


    return render_template('index.html', names = people)

@app.route('/login')
def loginPage():
    return render_template('login.html')