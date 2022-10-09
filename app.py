from os import getenv
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY") #"ed11831cb9d551ab242ccde932871fcc" #getenv("SECRET_KEY")
#app.config['SECRET_KEY'] = 'ed11831cb9d551ab242ccde932871fcc'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import routes