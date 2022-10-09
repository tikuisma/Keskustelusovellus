from app import app
from flask import Flask, render_template, url_for, flash, redirect, request
from form import Registration, Login
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import users

posts = [
    {'author': 'Tiina',
    'title': 'Terveys',
    'content': 'Liikunta',
    'date_posted': 'Sep 24, 2022'},
    {'author': 'Timo',
    'title': 'Harrastukset',
    'content': 'Jalkapallo',
    'date_posted': 'Sep 18, 2022'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='Meistä')

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = Registration(request.form)
    if form.validate() and request.method == "POST":
        username = form.username.data
        password = form.password2.data
        if users.register(username, password):
            flash('Thank you for joining us.')
            return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash("Your login was made successfully.")
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)