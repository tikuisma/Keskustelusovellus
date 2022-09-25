from os import getenv
from flask import Flask, render_template, url_for, flash, redirect, request
from form import Registration, Login
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ed11831cb9d551ab242ccde932871fcc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key = True)
  #  username = db.Column(db.String(20), unique=True)
   # password = db.Column(db.String(60), unique=True)
   # role = db.Column(db.String(2))
   # messages = db.relationship('Message', backref='author', lazy=True)

    #def __repr__(self, username, password):
     #   self.username = username
      #  self.password = password

       # return f"(Käyttäjä {self.username}, {self.role})"

#class Message(db.Model):
   # id = db.Column(db.Integer, primary_key = True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    #heading = db.Column(db.String(100), nullable=False)
    #date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #type_content = db.Column(db.text, nullable=False)

    #def __repr__(self):
     #   return f"(Viesti {self.heading}, {self.date})"

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
    form = Registration()
    if form.validate_on_submit():
        flash('Thank you for joining us.')
        username = form.username.data
        password = form.password2.data
        secret_password = generate_password_hash(password)
        #info = User(username=username, password=secret_password)
        """CREATE DATABASE"""
        try:
            sql = """INSERT INTO users (name, password)
            VALUES (:name, :password)"""
            db.session.execute(sql, {"name":username, "password":secret_password})
            db.session.commit()
        except:
            return False
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