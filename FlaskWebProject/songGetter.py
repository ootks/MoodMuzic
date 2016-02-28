import httplib, urllib, base64, binascii, json
import pyechonest

def getSongs(emotions):
    happiness = emotions['happiness']
    anger = emotions['anger']
    contempt = emotions['contempt']
    disgust = emotions['disgusts']
    fear = emotions['fear']
    sadness = emotions['sadness']
    surprise = emptions['sadness']
    biggestMood = max(happiness, sadness, anger)
    if biggestMood == happiness:
        mood = "happy"
    if biggestMood == sadness:
        mood = "sad"
    if biggestMood == anger:
        mood = "angry"


    max_tempo=None
    min_tempo=None
    max_loudness=None
    min_loudness=None

    min_energy=-max(fear, sadness, disgust)
    max_energy=max(happiness, anger, contempt, surprise)

    min_danceability=-max(fear, disgust, anger, contempt, sadness)
    max_danceability=max(happiness, surprise)

    max_acousticness=None
    min_acousticness=None

    max_liveness=None
    min_liveness=None

    max_valence=None
    min_valence=None

