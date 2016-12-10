from flask import Flask

app = Flask(__name__)

#  grab configuration stuff
app.config.from_object('config')

from app import views
