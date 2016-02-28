import httplib, urllib, base64, binascii, json, emotions
from pyechonest import song
from pyechonest import config 

def getSongs(emots):
    config.ECHO_NEST_API_KEY = "7UL5JWDT2WWMWSMYS"

    if u'faceRectangle' not in emots:
        return str(emots)
    emots = emots['scores']
    happiness = emots['happiness']
    anger = emots['anger']
    contempt = emots['contempt']
    disgust = emots['disgusts']
    fear = emots['fear']
    sadness = emots['sadness']
    surprise = emots['sadness']
    biggestMood = max(happiness, sadness, anger)
    if biggestMood == happiness:
        biggestMood = "happy"
    if biggestMood == sadness:
        biggestMood = "sad"
    if biggestMood == anger:
        biggestMood = "angry"


  #  max_tempo=None
  #  min_tempo=None
 #   max_loudness=None
 #   min_loudness=None

 #   min_energy=1-max(fear, sadness, disgust)
 #   max_energy=max(happiness, anger, contempt, surprise)

  #  min_danceability=1-max(fear, disgust, anger, contempt, sadness)
  #  max_danceability=max(happiness, surprise)

#    max_acousticness=None
#    min_acousticness=None

 #   max_liveness=None
#    min_liveness=None

#    max_valence=None
#    min_valence=None
#    return song.search(mood = mood, min_energy = min_energy, min_danceability = min_danceability, max_danceability = max_danceability)
    return song.search(mood = "happy")
