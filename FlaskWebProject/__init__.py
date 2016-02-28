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
SPOTIFY_CLIENT_ID = "90978a365a8e44f58aad6f13c21f8c82"
#import FlaskWebProject.views

@app.route('/')
def singlesong():
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
    if 'image' not in request.form:
        return "Darn"
    image = request.form['image']
    image = re.sub(".*base64,", "", image)
    image = base64.b64decode(image)
    emots = emotions.getEmotions(image)
    stoof = songs.getSongs(emots)
    track = stoof.get_tracks('spotify-WW')[0]
    return """<iframe src="https://embed.spotify.com/?uri="""+track['foreign_id']+"""" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>"""
#    return stoof.title
