from os import getenv
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

import routes