"""
The flask application package.
"""
import emotions, re, base64, sys, songs, spotipy
import spotipy.util as util
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

from pyechonest import config
config.ECHO_NEST_API_KEY = "7UL5JWDT2WWMWSMYS"
SpotifyKey = "90978a365a8e44f58aad6f13c21f8c82"
#import FlaskWebProject.views

@app.route('/')
def singlesong():
    util.prompt_for_user_token("ootks","playlist-modify-public")
    return render_template('singlesong.html')

@app.route('/video')
def home():
    return render_template('index.html')

@app.route('/getEmotions', methods = ['POST'])
def getEmotion():
    if 'image' not in request.form:
        return "fuck"
    image = request.form['image']
    image = re.sub(".*base64,", "", image)
    image = base64.b64decode(image)
    #return image
#    return "fuck"
#return image
    return str(emotions.getEmotions(image))

@app.route('/getSongs', methods = ['POST'])
def getSong():
	return "music"
    # if 'image' not in request.form:
    #     return "fuck"
    # image = request.form['image']
    # image = re.sub(".*base64,", "", image)
    # image = base64.b64decode(image)
    # emots = emotions.getEmotions(image)
    # print >> sys.stderr, str(emots)
    # print >> sys.stderr, str(type(emots))
    # stoof = str(songs.getSongs(emots))
    # print >> sys.stderr, stoof
    # return stoof
