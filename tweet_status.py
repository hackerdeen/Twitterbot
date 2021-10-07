import requests
import json
from time import time, sleep
import tweepy
import credentials

status = "https://hub.57north.org.uk/api/status/current"

consumer_key = credentials.API_key
consumer_secret_key = credentials.API_secret_key
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_status():
# polls the spi
    try:
        r = requests.get(status)
    except:
        print("Couldn't speak to API")

    res = json.loads(r.text)
    return res['result']

def state_change(state, lastState):
# checks if the state of the space has changed
    print ("s: " + str(state) + "ls: " + str(lastState))
    if state == lastState:
        return False
    else:
        return True

def send_tweet(status_track):
    state_array = get_status()
    state_bool = state_array['open']
    print("st :" + str(status_track))
    status_changed = state_change(state_bool, status_track)
    print("sc: " + str(status_changed))
    if status_changed == True:
        status_track = state_bool
        print("track: " + str(status_track))

    if state_bool==True:
        state = "opened"
    else:
        state = "closed"
    
    if status_changed==True:
        tweet = "Space " + state + " by " + state_array['trigger_person']+ " with message: " + state_array['message']
        print(tweet)
        try:
            api.update_status(tweet)
        except tweepy.TweepError as error:
            if error.api_code == 187:
                print("Already posted")
        else:
            print("Hey it tweeted OK")
    else:
        print("no change")
    
    return status_track

if __name__=="__main__":
    status_track = False
    while True:
        status_track = send_tweet(status_track)
        sleep(30)
