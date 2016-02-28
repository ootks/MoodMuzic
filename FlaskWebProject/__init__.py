"""
The flask application package.
"""
import emotions, re, base64, sys
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

from pyechonest import config
config.ECHO_NEST_API_KEY = "7UL5JWDT2WWMWSMYS"
#import FlaskWebProject.views

@app.route('/')
def singleframe():
    return render_template('singleframe.html')

@app.route('/video')
def home():
    return render_template('index.html')

@app.route('/getEmotions', methods = ['POST'])
def getEmotion():
    if 'image' not in request.form:
        return "fuck"
    image = request.form['image']
    image = re.sub(".*base64,", "", image)
#    image = base64.b64decode(image)
    return str(len(image))

#return image
#return str(emotions.getEmotions(image))
    
