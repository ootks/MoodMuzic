"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

#import FlaskWebProject.views

@app.route('/')
def hello_world():
    return "Hello World!"
